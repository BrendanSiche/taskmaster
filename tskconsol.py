import argparse, cmd,sys, signal, process, bidon, time,logging, logging.config

# RED = '91' , GREEN = '92' YELLOW = '93'
# BLUE = '94' CYAN = '96' MAGENTA = '35'

config = []

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

def close(self):
    if self.file:
        self.file.close()
        self.file = None

def restart_process(arg, conf):
    params = 0
    for elem in arg:
        params = arg.split()
    if params == 0:
        logging.error(f"\u271D Restart Cmd without Args")
        print(Tcolors.colorize(Tcolors.CRO + " == * /!\ Restart Command Needs A Program Name Valid: /!\ * == \n",91))
        print("\n")
        return (0)
    else:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
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
        print(Tcolors.colorize(Tcolors.CRO + " == * /!\ Stop Command Needs A Program Name Valid: /!\ * == \n",91))
        print("\n")
        return (0)
    else:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
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
        print(Tcolors.colorize(Tcolors.CRO + " == * /!\ Start Command Needs A Program Name Valid: /!\ * == \n",91))
        print("\n")
        return (0)
    else:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
            else:
                print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[cur]) + "\n",94))
                process.follow_conf_launch(config['programs'][params[cur]])
                #process.check_on_process(config['programs'][params[cur]])
            cur +=1
            print("\n")
        return (0)

def stat_process(arg, conf):
    params = 0
    for elem in arg:
        params = arg.split()
    print (params)
    if params == 0:
        cur = 0
        for elem in conf['programs']:
            print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(elem) + "\n",94))
            process.how_many_running(conf['programs'][elem])
            cur +=1
            print("\n")
        return (0)
    if len(params) == 1:
        if params[0] not in conf['programs']:
            logging.error(f"\u271D Program not found : {str(params[0])}")
            print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[0]) + "\n",91))
        else:
            print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[0]) + "\n",94))
            process.how_many_running(conf['programs'][params[0]])
        print("\n")
        return (0)
    if len(params) > 1:
        cur = 0
        for elem in params:
            if params[cur] not in conf['programs']:
                logging.error(f"\u271D Program not found : {str(params[cur])}")
                print(f"{Tcolors.CRO}", Tcolors.colorize(Tcolors.UDRL + " Program not found : " + str(params[cur]) + "\n",91))
            else:
                print(f"{Tcolors.GARR}",Tcolors.colorize(Tcolors.UDRL + " Program : " + str(params[cur]) + "\n",94))
                process.how_many_running(conf['programs'][params[cur]])
            cur +=1
            print("\n")
        return (0)

def setup_config():
    global config

    config = process.check_validfile()
    for key, value in config['programs'].items():
        print(Tcolors.colorize(key + " : \n",92))
        for k, elem in value.items():
            print("\t", Tcolors.colorize(str(k) + " : " + str(elem),94))
        print("\n")
    print(Tcolors.colorize(Tcolors.UDRL + " ... Config file Load ... \n", 91))
    logging.info(f"Config file Load")
    #logging.info(f'Thread : checking process {elem}')
    for key in config['programs']:
        numprocs = config['programs'][key]['numprocs']
        print("LOOOLLL", numprocs)
        logging.info(f"Exec Process : {config['programs'][key]}")
        logging.info(f"Numprocs : {numprocs}")
        if numprocs > 1:
            for x in range(numprocs):
                logging.info(f"Exec Process : {config['programs'][key]}")
                process.execute_subprocess(config['programs'][key])
        else:
            process.execute_subprocess(config['programs'][key])
    return config


class TskConsol(cmd.Cmd):
    prompt = f"{Tcolors.BLINK}\033[35m{Tcolors.BLD} Taskmaster BJ $> {Tcolors.CLR}"
    intro = f"\033[93m{Tcolors.BLD} ===== Taskmaster: another job control deamon ===== \n\
    \033[96m use '?' to view commands list or 'help <cmd>' to see the method of use a command\n{Tcolors.CLR}"
    global config
 
    count = 0
    file = None

    def init_tsk(self):
        logging.info('Initialisation Taskmaster')
        print(Tcolors.colorize(" == Config file == \n",93))
        config = setup_config()
        return config
        #print(Tcolors.colorize(" == Config file == \n",93))
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
        '\t\033[93m\033[1m quit/exit  : kill all process and quit taskmaster \n\033[94m| Usage : $> <quit>' 
        print(Tcolors.colorize("\t == * Quit/Exit * == ",35))
        print(Tcolors.colorize("\t == * Do you want quit Taskmaster? y/n * == ",35))
        print(Tcolors.colorize("\t == * All processes will be killed  * == ",35))
      # self.close()
      # force_kill si on veux 
        print("Bye!")
        return True
    def do_exit(self,arg):
        '\t\033[93m\033[1m quit/exit  : kill all process and quit taskmaster \n\033[94m| Usage : $> <exit>' 
        self.do_quit(arg)
        return True
    def do_EOF(self,arg):
        return True
    def handler(signum, frame):
        print(Tcolors.colorize("\t == * Caught CTRL-C, press enter to continue or exit/quit to leave* == \n", 91))
    signal.signal(signal.SIGINT, handler)

def loop():
    config = TskConsol().init_tsk()
    thr = bidon.Thr(1,"th1",config)
    thr.daemon = True
    thr.start()
    logging.info('Starting Thread')
    print("in loop")
    TskConsol().cmdloop()

    print("end loop")


