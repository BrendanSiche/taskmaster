import argparse, cmd

class Tcolors():
    BOLD = '\033[1m'
    CLEAR = '\033[0m'
    UNDERLINE = '\033[4m'
    BLINK = "\033[5m"
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[35m'

class TskConsol(cmd.Cmd):
    prompt = f"{Tcolors.BLINK}{Tcolors.MAGENTA}{Tcolors.BOLD} Taskmaster BJ $> {Tcolors.CLEAR}"
    intro =  f"{Tcolors.YELLOW}{Tcolors.BOLD} ===== Taskmaster: another job control deamon ===== \n\
    {Tcolors.CYAN}use 'usage' to view commands list or 'help <cmd>' to see the method of use a command\n{Tcolors.CLEAR}"
   
    def do_error(self,param):
        print(f"{Tcolors.RED}{Tcolors.BOLD}{param}{Tcolors.CLEAR}")

    def do_help(self,param):
        print(f"{Tcolors.RED}{Tcolors.BOLD}LOOOLLL{param}{Tcolors.CLEAR}")
   

#TskConsol().cmdloop()
