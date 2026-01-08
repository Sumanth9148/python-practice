from multiprocessing import Process
import time

def task1():
    for i in range(4):
        print("1st process")
        time.sleep(0.8)

def task2():
    for i in range(4):
        print("2nd process")
    time.sleep(0.8)


if __name__=="__main__":

    p1=Process(target=task1)
    p2=Process(target=task2)

    p1.start()
    p1.join()
    p2.start()

    # p1.join()
    p2.join()

    print("main")

