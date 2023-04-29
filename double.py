def double(funct):
    def modify():
        funct()
        print("Let's try that again!")
        funct()
    return modify
