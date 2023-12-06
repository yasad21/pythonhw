import time

def timestamp(f):
    def inner():
        print(time.ctime())
        f()
    return inner
