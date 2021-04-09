import threading, time, process, logging

class Thr(threading.Thread):
    global config
    def __init__(self, thrID, name,conf):
        threading.Thread.__init__(self)
        logging.info(f'Thread : Id: {thrID} Name: {name} Conf: {conf}')
        self.thrID = thrID
        self.name = name
        self.config = conf
    def run (self):
        print("starting Thread" + self.name)
        while 1 :
            time.sleep(2)
            process.background_check(self.config)
        print_time(self.name)
        print("extir thread" + self.name)
        logging.info(f'Thread : Exit thread {self.name}')

def print_time(thrname):
    time.sleep(0.3)
    print(thrname, time.ctime(time.time()))