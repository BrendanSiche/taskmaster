import yaml, subprocess, time, os
from datetime import datetime

running = {}
session_history = {}
should_be_running = []

with open("conf.yaml", 'r') as f:
    config = yaml.safe_load(f)

def check_config():
    for elem in config['programs']:
        if (config['programs'][elem].get('stdout') != None and config['programs'][elem].get('stderr') == None) or (config['programs'][elem].get('stderr') != None and config['programs'][elem].get('stdout') == None):
            print('If you set one of stderr/stdout, you need to set both')
            exit()

def check_file(path):
    if path == None:
        return(False)
    if os.path.exists(path):
        if os.path.isfile(path):
            return os.access(path, os.W_OK)
        else:
            return False
    parent = os.path.dirname(path)
    if not parent: 
        parent = '.'
    return os.access(parent, os.W_OK)

def execute_subprocess(param):
    if param['cmd'] not in running:
        running[param['cmd']] = []
    new = {}
    cmd = param['cmd'].split(' ')
    string = ''
    cwd = param['workingdir'] if param['workingdir'] else None     
    umsk = param['umask'] if param['umask'] else -1
    if check_file(param.get('stdout')) and check_file(param.get('stderr')):
        with open(param['stdout'], 'a') as sout, open(param['stderr'], 'a') as serr:
            process = subprocess.Popen(cmd, cwd=cwd, stdout=sout, stderr=serr, umask=umsk)
    else:
        process = subprocess.Popen(cmd, cwd=cwd, umask=umsk)
    pname = param['cmd'] + ' process number: ' + str(len(running[param['cmd']]))
    new['id'] = pname
    new['process'] = process
    new['conf'] = param
    new['start_time'] = datetime.now()
    running[param['cmd']].append(new)


def check_time(first, second):
    now = datetime.now()
    diff = now - first
    print('Timecheck = ', diff.seconds)
    if(diff.seconds >= second):
        return(True)
    return(False)

def how_many_running(param):
    cur = 0
    done = 0
    new_running = []
    ran = []
    name = param['cmd']
    if running.get(name) == None:
        return(0)
    for elem in running[name]:
        if elem['process'].poll() != None:
            if name not in session_history:
                session_history[name] = []
            session_history[name].append(elem)
            ran.append(elem)
            done += 1
            print('No more a')
        else:
            if check_time(elem['start_time'], param['starttime']) == True: 
                elem['confirm'] = 'True'
            new_running.append(elem)
            cur += 1
    running[name] = new_running
    print(done, ' process of ', name, 'have been succesfully executed')
    print(cur, ' process of ', name, 'still running')
    return(ran,done,cur)

def check_on_process(param):
    ran, done, cur = how_many_running(param)
    for elem in ran:
        if elem['process'].poll() not in param['exitcodes']:
            error = 'Error : Process ' + param['cmd'] + ' of pid '  + str(elem['process'].pid)  + ' exited with code: ' + str(elem['process'].poll())
            print(error)
            if param['autorestart'] == 'unexpected':
                print('relaunching process following unexpected end')
                execute_subprocess(param)
        else:
            if param['autorestart']:
                print('relaunching process as expected')
                execute_subprocess(param)
        if param.get('starttime') != None and elem.get('confirm') == None:
            error = 'Error : Process ' + param['cmd'] + ' of pid '  + str(elem['process'].pid)  + ' exited with code: ' + str(elem['process'].poll()) + ' before reaching set start time'
            print(error)

def follow_conf_launch(param):
    i = how_many_running(param)
    j = param['numprocs']
    j = j - i
    for x in range(j):
        execute_subprocess(param)

def grace_kill(param):
    cur = 0
    done = 0
    new_running = []
    ran = []
    name = param['cmd']
    check_on_process(param)
    if running.get(name) == None:
        return(0)
    for elem in running[name]:
        print('killing a')
        elem['process'].kill()
        time.sleep(1)
        print(elem['process'].poll())
    return(0)



check_config()
execute_subprocess(config['programs']['a.out'])
print('launched')
check_on_process(config['programs']['a.out'])
time.sleep(3)
print('checked')
grace_kill(config['programs']['a.out'])
print('killed')
check_on_process(config['programs']['a.out'])