from threading import *
import time

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            time.sleep(0.3)


class hi(Thread):
    def run(self):
        a=input("enter name: ")
        print("hii",a)
        time.sleep(0.8)
        # for i in range(5):
        #     print("hi")
        #     time.sleep(0.5)

o1=hello()
o2=hi()


o1.start()     #thread 1
o1.join()     #makes finish one thread completely and then goes for next thread
o2.start()     #thread 2

o2.join()

print("bye")     #main thread


#without thread
# o2.greeting()
# o1.greet()
