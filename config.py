import yaml, os, sys, array
from tskconsol import Tcolors

class Config():
    
    def p_error(param):
        print(f"{Tcolors.RED}{Tcolors.BOLD}Invalid config file: /!\ {param}{Tcolors.CLEAR}")

    def creat_defconfig():
        default_conf = {
            'General': {
                'jsp': 'lol'
            },
            'programs': {
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
                }
            }
        with open('defconf.yaml', 'w') as yaml_file:
            yaml.dump(default_conf, yaml_file, default_flow_style=False)
            return yaml_file 

    def check_val(config, tag, val, type):
        for key in config[tag] :
            if key == val:
                ret = config[tag][key]
                if isinstance(ret, int):
                    if ret < 0:
                        err =' --> '+ tag + ': ' + '{ '+ key + ' }' + ' Invalid type : ' + str(ret) + ' Expected type: not neg val'
                        Config.p_error(err)
                        return False
                if isinstance(ret, type):
                    if key == "autorestart":
                        if ret != "unexpected" and ret != "always" and ret != "never":
                            err =' --> '+ tag + ': ' + '{ '+ key + ' }' + ' Invalid value : ' + str(ret) + ' Expected type: unexpected/always/never'
                            Config.p_error(err)
                            return False
                    return True
                else:
                    err =' --> '+ tag + ': ' + '{ '+ key + ' }' + ' Invalid type : ' + str(ret) + ' Expected type: ' + str(type)
                    Config.p_error(err)
        return False

    def check_validfile():
        values = {"autorestart": str,
            "autostart": bool,
            "cmd": str,
            "exitcodes": list,
            "numprocs": int,
            "startretries": int,
            "starttime": int,
            "stderr": str,
            "stdout": str,
            "stopsignal": str,
            "stoptime": int,
            "umask": int,
            "workingdir": str,}
        if len(sys.argv) == 2:
            arg = sys.argv[1]
        else:
            Config.creat_defconfig()
            arg = 'defconf.yaml'
        with open(arg, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
        for key in config :
            if key != "General" and key != "programs":
                Config.p_error(key)
                break
            if key != "programs" and key != "General":
                Config.p_error(key)
                break
        for key in values:
            Config.check_val(config,'programs', key, values[key])

Config.check_validfile()
