import threading, time

class Thr(threading.Thread):
    def __init__(self, thrID, name,count):
        threading.Thread.__init__(self)
        self.thrID = thrID
        self.name = name
        self.count = count
    def run (self):
        print("starting Thread" + self.name)
        print_time(self.name, self.count, 0.1)
        print("extir thread" + self.name)

def print_time(thrname,count, delay):
    while count:
        if exitFlag:
            threadName.exit()
    time.sleep(delay)
    print(thrname, time.ctime(time.time()))
    count -= 1