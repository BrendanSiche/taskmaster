import yaml, os, sys, tskconsol

class Config():
    
    def p_error(param):
        print(f"\t{tskconsol.CRO} ", tskconsol.Tcolors.colorize(" == * Invalid config file: /!\ --> " +param+" * == \n",91))
       # print(f"{tskconsol.Tcolors.RED}{tskconsol.Tcolors.BLD}Invalid config file: /!\ {param}{tskconsol.Tcolors.CLR}")

    def creat_defconfig():
        default_conf = {
            'General': {
                'jsp': 'lol'
            },
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
                    "starttime" : 5,
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
                    "starttime" : 5,
                    "stopsignal" : 'TERM',
                    "stoptime" : 10,
                    "stdout" : '/tmp/pwd.stdout',
                    "stderr" : '/tmp/pwd.stderr',
                }
                }
            }
        with open('defconf.yaml', 'w') as yaml_file:
            yaml.dump(default_conf, yaml_file, default_flow_style=False)
        print(f"\t {tskconsol.Tcolors.GARR} ", tskconsol.Tcolors.colorize(" == * Config file Created: ->' defconf.yaml '" +" * == \n",91))
        #print(f"{tskconsol.Tcolors.GREEN}{tskconsol.Tcolors.BLD} Config file Created: /!\ ' defconf.yaml '\n{tskconsol.Tcolors.CLR}")
        return yaml_file 

    def check_val(param, val):
        for key in param:
            if key not in val:
                err =' --> '+ key
                Config.p_error(err)
                return False
            if isinstance(param[key], int):
                if param[key] < 0:
                    err =' -->'+ key + ' Invalid value : '+ str(param[key]) + ' Expected type: not neg val'
                    Config.p_error(err)
                return False
            if isinstance(param[key], val[key]):
                if param[key] == "autorestart":
                    if param[key] != "unexpected" and param[key] != "always" and param[key] != "never":
                        err =' --> '+ key + ' Invalid value : ' + param[key] + ' Expected type: unexpected/always/never'
                        Config.p_error(err)
                        return False
            return True