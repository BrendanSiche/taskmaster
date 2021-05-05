import argparse, cmd, sys, signal, process, tools, time, logging, logging.config

# RED = '91' , GREEN = '92' YELLOW = '93'
# BLUE = '94' CYAN = '96' MAGENTA = '35'

config = []
completion = []

class Tcolors():
    BLD = '\033[1m'
    CLR = '\033[0m'
    UDRL = '\033[4m'
    BLINK = "\033[5m"
    GARR = '\033[92m \u2714'
    CRO = '\033[91m\033[1m \u271D'
    ST = "\033[93m\u231B\033[0m"
    ESCAPE = '%s[' % chr(27)
    RESET = '%s0m' % ESCAPE
    FORMAT = '1;%dm'

    def colorize(text, color):
        return Tcolors.ESCAPE + (Tcolors.FORMAT % (color, )) + text + Tcolors.RESET

def close(config):
    while 1:
        inpt = input('Do you want kill all process? y/n ')
        if inpt == 'yes' or inpt == 'y':
            tools.kill_it_with_fire(config)
            exit()
        elif inpt == 'no' or inpt == 'n':
            exit()
        elif inpt != 'yes' or inpt != 'y' or inpt != 'no' or inpt != 'n':
            print(Tcolors.colorize("\t Bad input answer yes/no ",35))

def restart_process(arg, conf):
    params = 0
    for elem in arg:
        params = arg.split()
    if params == 0:
        logging.error(f"\u271D Restart Cmd without Args")
        tools.log_mail('tskbidon@gmail.com', 'Restart Cmd without Args')
        print(Tcolors.colorize(Tcolors.CRO + " == * /!\ Restart Command Needs A Program Name Valid: /!\ * == \n",91))
        print("\n")
        return (0)
    else:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
                err = " Program not found = " + str(params[cur])
                tools.log_mail('tskbidon@gmail.com', err)
            else:
                print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[cur]) + "\n",94))
                process.grace_kill(config['programs'][params[cur]])
                time.sleep(0.2)
                ret = process.how_many_running(config['programs'][params[cur]])[2]
                if ret > 0:
                    process.force_kill(config['programs'][params[cur]])
                logging.info(f"Restarting Process : {config['programs'][params[cur]]}")
                process.follow_conf_launch(config['programs'][params[cur]])
            cur +=1
            print("\n")
        return (0)

def stop_process(arg, conf):
    params = 0
    for elem in arg:
        params = arg.split()
    if params == 0:
        logging.error(f"\u271D Stop Cmd without Args")
        tools.log_mail('tskbidon@gmail.com', 'Stop Cmd without Args')
        print(Tcolors.colorize(Tcolors.CRO + " == * /!\ Stop Command Needs A Program Name Valid: /!\ * == \n",91))
        print("\n")
        return (0)
    else:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                err = " Program not found = " + str(params[cur])
                tools.log_mail('tskbidon@gmail.com', err)
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
            else:
                print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[cur]) + "\n",94))
                process.grace_kill(config['programs'][params[cur]])
            cur +=1
            print("\n")
        return (0)

def start_process(arg,conf):
    params = 0
    for elem in arg:
        params = arg.split()
    if params == 0:
        logging.error(f"\u271D Start Cmd without Args")
        tools.log_mail('tskbidon@gmail.com', 'Start Cmd without Args')
        print(Tcolors.colorize(Tcolors.CRO + " == * /!\ Start Command Needs A Program Name Valid: /!\ * == \n",91))
        print("\n")
        return (0)
    else:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
                err = " Program not found = " + str(params[cur])
                tools.log_mail('tskbidon@gmail.com', err)
            else:
                print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[cur]) + "\n",94))
                process.follow_conf_launch(config['programs'][params[cur]])
            cur +=1
            print("\n")
        return (0)

def stat_process(arg, conf):
    params = 0
    for elem in arg:
        params = arg.split()
    if params == 0:
        cur = 0
        for elem in conf['programs']:
            print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(elem) + "\n",94))
            ran = process.how_many_running(conf['programs'][elem])[2]
            cur +=1
            print(ran, "\n")
        return (0)
    if len(params) == 1:
        if params[0] not in conf['programs']:
            logging.error(f"\u271D Program not found : {str(params[0])}")
            err = " Program not found = " + str(params[cur])
            tools.log_mail('tskbidon@gmail.com', err)
            print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[0]) + "\n",91))
        else:
            print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[0]) + "\n",94))
            ran = process.how_many_running(conf['programs'][params[0]])[2]
        print(ran, "\n")
        return (0)
    if len(params) > 1:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
                err = " Program not found = " + str(params[cur])
                tools.log_mail('tskbidon@gmail.com', err)
            else:
                print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[cur]) + "\n",94))
                ran = process.how_many_running(conf['programs'][params[cur]])[2]
            cur +=1
            print(ran, "\n")
        return (0)

def update_config():
    global config
    relaunch = ['cmd', 'umask', 'workingdir', 'env', 'stdout', 'stderr']

    config['runing'] = 0
    new = process.check_validfile(1)
    for key in new['programs']:
        if key in config['programs']:
            diffkey = [k for k in config['programs'][key] if config['programs'][key][k] != new['programs'][key][k]]
            check = any(item in diffkey for item in relaunch)
            if check == True and process.how_many_running(config['programs'][key])[2] > 0:
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Warning : The process " + key + " will have to be restarded, due to change made in the config file\n",91))
                process.force_kill(config['programs'][key])
            config['programs'][key].update(new['programs'][key])
        else:
            config['programs'][key] = new['programs'][key]
    for key, value in config['programs'].items():
        print(Tcolors.colorize(key + " : \n",92))
        for k, elem in value.items():
            print("\t", Tcolors.colorize(str(k) + " : " + str(elem),94))
        print("\n")
    print(Tcolors.colorize(Tcolors.UDRL + " ... Config file Load ... \n", 91))
    logging.info(f"Config file Load")
    for key in config['programs']:
        if config['programs'][key].get('autostart') == 'true' or config['programs'][key].get('autostart') == 'true':
            process.follow_conf_launch(config['programs'][key])
    completion = []
    for elem in config['programs']:
        completion.append(elem)
    config['runing'] = 1
    return(config)

def setup_config():
    global config
    global completion

    if len(config) > 0:
        config = update_config()
        return(config)
    else:
        config = process.check_validfile()
    if config == None:
        print(Tcolors.colorize(Tcolors.UDRL + "Error Config file ... \n", 91))
        logging.error(f"Error Config file ")
    for key, value in config['programs'].items():
        print(Tcolors.colorize(key + " : \n",92))
        for k, elem in value.items():
            print("\t", Tcolors.colorize(str(k) + " : " + str(elem),94))
        print("\n")
    print(Tcolors.colorize(Tcolors.UDRL + " ... Config file Load ... \n", 91))
    logging.info(f"Config file Load")
    for key in config['programs']:
        if config['programs'][key].get('autostart') == 'true' or config['programs'][key].get('autostart') == 'true':
            process.follow_conf_launch(config['programs'][key])
    completion = []
    for elem in config['programs']:
        completion.append(elem)
    return config


class TskConsol(cmd.Cmd):
    prompt = f"{Tcolors.BLINK}\033[35m{Tcolors.BLD} Taskmaster BJ $> {Tcolors.CLR}"
    intro = f"\033[93m{Tcolors.BLD} ===== Taskmaster: another job control deamon ===== \n\
    \033[96m use '?' to view commands list or 'help <cmd>' to see the method of use a command\n{Tcolors.CLR}"
    global config
    global completion
 
    def init_tsk(self):
        logging.info('Initialisation Taskmaster')
        tools.log_mail('tskbidon@gmail.com', 'Initialisation Taskmaster')
        print(Tcolors.colorize(" == Config file == \n",93))
        config = setup_config()
        return config
    def do_status(self,arg):
        '\t\033[93m\033[1m status: shows all controlled process \n\033[94m| Usage for all: $> <status> \n| Usage for specific(s) process: $> <status [process1 ...]>' 
        print(Tcolors.colorize("\t == * Status * == \n",35))
        stat_process(arg, config)
    def do_start(self,arg):
        '\t\033[93m\033[1m start: running job \n\033[94m| Usage : $> <start [process ...]>' 
        print(Tcolors.colorize("\t == * Start * == \n",35))
        start_process(arg,config)
    def do_stop(self,arg):
        '\t\033[93m\033[1m stop: stop job \n\033[94m| Usage : $> <stop [process ...]>' 
        print(Tcolors.colorize("\t == * Stop * == \n",35))
        stop_process(arg, config)
    def do_restart(self,arg):
        '\t\033[93m\033[1m restart: restart job \n\033[94m| Usage : $> <restart [process ...]>' 
        print(Tcolors.colorize("\t == * Restart * == \n",35))
        restart_process(arg, config)
    def do_reload(self,arg):
        '\t\033[93m\033[1m reload  : reload cconfig file \n\033[94m| Usage : $> <reload [process ...]>' 
        print(Tcolors.colorize("\t == * Reload * == \n",35))
        logging.warning('Reloadig Config File')
        config = self.init_tsk()
    def do_quit(self,arg):
        logging.warning('Exit/Quit Taskmaster')
        tools.log_mail('tskbidon@gmail.com', 'Exit/Quit Taskmaster')
        '\t\033[93m\033[1m quit/exit  : Quit taskmaster \n\033[94m| Usage : $> <quit>' 
        print(Tcolors.colorize("\t == * Quit/Exit * == ",35))
        print(Tcolors.colorize("\t == * Do you want kill all process? y/n * == ",35))
        print(Tcolors.colorize("Warning: If all process are not closed within 3 seconds after their gracefull kill, they will be force killed using SIGTERM \t  ",35))
        close(config)
        print("Bye!")
        return True
    def do_exit(self,arg):
        '\t\033[93m\033[1m quit/exit  : kill all process and quit taskmaster \n\033[94m| Usage : $> <exit>' 
        self.do_quit(arg)
        return True
    def complete_start(self, text, line, begidx, endidx):
        if not text:
            complete = completion
        else:
            complete = [ f
                            for f in completion
                            if f.startswith(text)
                            ]
        return completion
    def complete_stop(self, text, line, begidx, endidx):
        if not text:
            complete = completion
        else:
            complete = [ f
                            for f in completion
                            if f.startswith(text)
                            ]
        return completion
    def complete_restart(self, text, line, begidx, endidx):
        if not text:
            complete = completion
        else:
            complete = [ f
                            for f in completion
                            if f.startswith(text)
                            ]
        return completion
    def complete_status(self, text, line, begidx, endidx):
        if not text:
            complete = completion
        else:
            complete = [ f
                            for f in completion
                            if f.startswith(text)
                            ]
        return completion
    def handler(signum, frame):
        print(Tcolors.colorize("\t == * Caught CTRL-C, press enter to continue or exit/quit to leave* == \n", 91))
    signal.signal(signal.SIGINT, handler)

def loop():
    config = TskConsol().init_tsk()
    thr = tools.Thr(1,"th1",config)
    thr.daemon = True
    thr.start()
    logging.info('Starting Thread')
    TskConsol().cmdloop()


