import yaml, subprocess, time, os, sys, signal
from datetime import datetime
from config import Config
import tskconsol
import process

running = {}
session_history = {}
should_be_running = []

#for i in {0..256};do o=00$i;echo -ne "${o:${#o}-3:3} "$(tput setaf $i;tput setab $i)"   "$(tput sgr0);done; 


#config = Config.check_validfile()

#with open("conf.yaml", 'r') as f:
 #   config = yaml.safe_load(f)

#for i in range(150):
   # print()
  #  i += 1


#{Tcolors.RED}{Tcolors.BLD} Program don't found : {params[0]}{Tcolors.CLR}")
def init():
    tskconsol.loop()
    #tskconsol.TskConsol().cmdloop()
init()

#execute_subprocess(config['programs']['ls'])
#execute_subprocess(config['programs']['a.out'])
#
# execute_subprocess(config['programs']['a.out'])
#
# print('launched')
#check_on_process(config['programs']['a.out'])
#time.sleep(3)
#print('checked')
#grace_kill(config['programs']['a.out'])
#print('pretend to be killed')
#time.sleep(1)
#check_on_process(config['programs']['a.out'])
#print('Checked once')
#time.sleep(5)
#print('Checked twice')
#check_on_process(config['programs']['a.out'])
