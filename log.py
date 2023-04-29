import time

def timestamp(funct):
    def modify():
        print(time.ctime())
        funct()
    return modify
