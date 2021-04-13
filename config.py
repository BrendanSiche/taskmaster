import yaml, os, sys, tskconsol, logging, tools

class Config():
    
    def p_error(param):
        print(f"\t{tskconsol.CRO} ", tskconsol.Tcolors.colorize(" == * Invalid config file: /!\ --> " +param+" * == \n",91))

    def creat_defconfig():
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
                }
                }
            }
        with open('defconf.yaml', 'w') as yaml_file:
            yaml.dump(default_conf, yaml_file, default_flow_style=False)
        logging.warning(f"Config : Default Config file Created: -> 'defconf.yaml'")
        tools.log_mail('tskbidon@gmail.com', "Config : Default Config file Created: -> 'defconf.yaml'")
        print(f"\t {tskconsol.Tcolors.GARR} ", tskconsol.Tcolors.colorize(" == * Config file Created: ->' defconf.yaml '" +" * == \n",91))
        return yaml_file 

    def check_val(param, val):
        for key in param:
            if key not in val:
                err =' --> '+ key
                Config.p_error(err)
                return False
            if isinstance(param[key], int):
                if param[key] < 0:
                    err ='Error: -->'+ key + ' Invalid value : '+ str(param[key]) + ' Expected type: not neg val'
                    tools.log_mail('tskbidon@gmail.com', err)
                    Config.p_error(err)
                return False
            if isinstance(param[key], val[key]):
                if param[key] == "autorestart":
                    if param[key] != "unexpected" and param[key] != "always" and param[key] != "never":
                        err ='Error: --> '+ key + ' Invalid value : ' + param[key] + ' Expected type: unexpected/always/never'
                        tools.log_mail('tskbidon@gmail.com', err)
                        Config.p_error(err)
                        return False
            return True