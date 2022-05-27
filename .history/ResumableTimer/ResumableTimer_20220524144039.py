from threading import Timer
import time

class ResumableTimer(object):

    def __init__(self, timeout, callback,args = None,kwargs = None):
        self.timer = Timer(timeout, callback,args,kwargs)
        self.args_argument = args
        self.kwargs_argument = kwargs
        self.start_time = None
        self.cancel_time = None

        # Used for creating a new timer upon renewal
        self.timeout = timeout
        self.callback = callback

    def cancel(self):
        self.timer.cancel()

    def start(self):
        # NOTE: erroneously calling this after pausing causes errors where
        # start_time is updated, and then you get a RuntimeError
        # for trying to restart a thread
        self.start_time = time.time()
        self.timer.start()

    def pause(self):
        self.cancel_time = time.time()
        self.timer.cancel()
        return self.get_remaining_time()

    def resume(self):
        self.timeout = self.get_remaining_time()
        self.timer = Timer(self.timeout, self.callback)
        self.start_time = time.time()
        self.timer.start()

    def get_remaining_time(self):
        if self.start_time is None or self.cancel_time is None:
            return self.timeout
        return self.timeout - (self.cancel_time - self.start_time)

if __name__ == "__main__":
    def f(num):
        print('Hello there ' + str(num))
    
    t = ResumableTimer(5,f,[2])
    t.start()
    time.sleep(1)
    print(t.pause())
    time.sleep(3)
    t.resume()