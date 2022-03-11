from threading import *
import time
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
t1.join()
t2.join()
print("Bye")