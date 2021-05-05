import yaml, os, sys, tskconsol, logging, tools

def log_and_print(err):
    print(f"{tskconsol.Tcolors.CRO}", tskconsol.Tcolors.colorize(tskconsol.Tcolors.UDRL + " Ivalid Config File :" + err + "\n",91))
    logging.error(f"\u271D Ivalid Config File :" + err)
    tools.log_mail('tskbidon@gmail.com', "Ivalid Config File = " + err )
    exit()


class Config():
    
    def p_error(param):
        print(f"\t{tskconsol.CRO} ", tskconsol.Tcolors.colorize(" == * Invalid config file: /!\ --> " +param+" * == \n",91))

    def creat_defconfig(switch = None):
        default_conf = {
            'programs': {
                'ls': {
                    'cmd' : '/bin/ls',
                    'numprocs' : 1,
                    "umask" : 0o22,
                    "workingdir" : '/tmp',
                    "autostart" : 'true',
                    "autorestart" : 'unexpected',
                    "exitcodes" : [0,2],
                    "startretries" : 3,
                    "starttime" : 0,
                    "stopsignal" : 'TERM',
                    "stoptime" : 10,
                    "stdout" : '/tmp/ls.stdout',
                    "stderr" : '/tmp/ls.stderr',
                    "env":
                        {"STARTED_BY": "taskmaster"},
                    },
                'pwd' : {
                    'cmd' : '/bin/pwd',
                    'numprocs' : 1,
                    "umask" : 0o22,
                    "workingdir" : '/tmp',
                    "autostart" : 'true',
                    "autorestart" : 'unexpected',
                    "exitcodes" : [0,2],
                    "startretries" : 3,
                    "starttime" : 0,
                    "stopsignal" : 'TERM',
                    "stoptime" : 10,
                    "stdout" : '/tmp/pwd.stdout',
                    "stderr" : '/tmp/pwd.stderr',
                    "env":
                        {"STARTED_BY": "taskmaster"},
                }
                }
            }
        with open('defconf.yaml', 'w') as yaml_file:
            yaml.dump(default_conf, yaml_file, default_flow_style=False)
        logging.warning(f"Config : Default Config file Created: -> 'defconf.yaml'")
        tools.log_mail('tskbidon@gmail.com', "Default Config file Created = defconf.yaml")
        print(f"\t {tskconsol.Tcolors.GARR} ", tskconsol.Tcolors.colorize(" == * Config file Created: ->' defconf.yaml '" +" * == \n",91))
        return yaml_file 

    def check_config(config):
        for elem in config['programs']:
            if config['programs'][elem].get('cmd') == None or type(config['programs'][elem].get('cmd')) != str:
                log_and_print(elem + " invalid cmd parameter")
            if config['programs'][elem].get('autostart') != None and type(config['programs'][elem].get('autostart')) != str:
                log_and_print(elem + " The auttostart parameter must be a bool (true or false)")
            if config['programs'][elem].get('autorestart') != None and type(config['programs'][elem].get('autorestart')) != str:
                print(type(config['programs'][elem].get('autorestart')))
                log_and_print(elem + " The autorestart parameter must be set to true/false/unexpected")
            if config['programs'][elem].get('exitcode') != None:
                if type(config['programs'][elem].get('exitcodes')) != list:
                    log_and_print(elem + " The exitcode parameter must be a list of int")
                for elem in config['programs'][elem]['exitcodes']:
                    if type(elem) != int:
                        log_and_print(elem + " The exitcode parameter must be a list of int")
            if config['programs'][elem].get('numprocs') != None:
                if type(config['programs'][elem].get('numprocs')) != int:
                    log_and_print(elem + " The numprocs parameter must be a positive int")
                if config['programs'][elem]['numprocs']  < 1:
                    log_and_print(elem + " The numprocs parameter must be a positive int")
            if config['programs'][elem].get('numprocs') == None:
                    config['programs'][elem]['numprocs'] = 1
            if config['programs'][elem].get('stoptime') != None:
                if type(config['programs'][elem].get('stoptime')) != int:
                    log_and_print(elem + " The stoptime parameter must be a positive int")
                if config['programs'][elem]['stoptime']  < 1:
                    log_and_print(elem + " The stoptime parameter must be a positive int")
            if config['programs'][elem].get('starttime') != None: 
                if type(config['programs'][elem].get('starttime')) != int:
                    log_and_print(elem + " The starttime parameter must be a positive or null int")
                if config['programs'][elem]['starttime']  < 0:
                    log_and_print(elem + " The starttime parameter must be a positive or null int")
            if config['programs'][elem].get('env') != None and type(config['programs'][elem].get('env')) != dict:
                log_and_print(elem + " The env parameter must be a dictionary")
            if (config['programs'][elem].get('stdout') != None and config['programs'][elem].get('stderr') == None) or (config['programs'][elem].get('stderr') != None and config['programs'][elem].get('stdout') == None):
                print(f"{tskconsol.Tcolors.CRO}", tskconsol.Tcolors.colorize(tskconsol.Tcolors.UDRL + " Ivalid Config File : If you set one of stderr/stdout, you need to set both \n",91))
                logging.error(f"\u271D Ivalid Config File : If you set one of stderr/stdout, you need to set both")
                tools.log_mail('tskbidon@gmail.com', "Ivalid Config File = If you set one of stderr/stdout, you need to set both")
                return False
        return True


    def check_val(param, val):
        for key in param:
            if key not in val:
                err =' --> '+ key
                Config.p_error(err)
                return False
        return True