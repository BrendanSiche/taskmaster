import yaml, subprocess, time, os

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
    new['start_time'] = time.time()
    running[param['cmd']].append(new)

def how_many_running(name):
    cur = 0
    done = 0
    new_running = []
    ran = []
    for elem in running[name]:
        if elem['process'].poll() == 0:
            if name not in session_history:
                session_history[name] = []
            session_history[name].append(elem)
            done += 1
        else:
            new_running.append(elem)
            cur += 1
    running[name] = new_running
    print(done, ' process of ', name, 'have been succesfully executed')
    print(cur, ' process of ', name, 'still running')

def check_on_process(param):
    how_many_running(param['cmd'])

check_config()
execute_subprocess(config['programs']['ls'])
execute_subprocess(config['programs']['ls'])
execute_subprocess(config['programs']['ls'])
time.sleep(1)
check_on_process(config['programs']['ls'])
time.sleep(1)
check_on_process(config['programs']['ls'])