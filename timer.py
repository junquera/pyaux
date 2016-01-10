import time

class Timer:
    def __init__(self):
        self.startTime = time.time()

    def start(self):
        self.startTime = time.time()

    def now(self):
        return time.time() - self.startTime

    def __repr__(self):
        hours, rem = divmod(self.now(), 3600)
        minutes, seconds = divmod(rem, 60)
        return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
