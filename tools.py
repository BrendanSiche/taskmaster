import threading, time, process, logging, smtplib, process

def kill_it_with_fire(config):
    cur = 0
    config['runing'] = 0
    for elem in config['programs']:
        process.grace_kill(config['programs'][elem])
    for elem in config['programs']:
        cur += process.how_many_running(config['programs'][elem])[2]
    if cur != 0:
        time.sleep(3)
        for elem in config['programs']:
            process.force_kill(config['programs'][elem])

def log_mail(toaddrs, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('tskbidon@gmail.com', 'Lalicorne')  
    server.sendmail('tskbidon@gmail.com', toaddrs, msg)  
    server.quit()

class Thr(threading.Thread):
    global config
    def __init__(self, thrID, name,conf):
        threading.Thread.__init__(self)
        logging.info(f'Thread : Id: {thrID} Name: {name} Conf: {conf}')
        self.thrID = thrID
        self.name = name
        self.config = conf
    def run (self):
        while 1:
            time.sleep(2)
            process.background_check(self.config)
        print_time(self.name)
        logging.info(f'Thread : Exit thread {self.name}')

def print_time(thrname):
    time.sleep(0.3)
    print(thrname, time.ctime(time.time()))