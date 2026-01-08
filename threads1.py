# print('a')
# print('b')
# print('c')




# import time

# print("start")
# time.sleep(4)
# print("end")




#without thread
# def work():
#     print("work start")
#     print("work end")

# work()
# print("main done")     #waits for work to finish





#with thread
import threading
# import time

def work():
    # time.sleep(2)
    print(6/0)
    

t1=threading.Thread(target=work)

def p1():
    print("main done") 

t1.start()          #wont waits for work to finish , both runs independently

# work()
p1()
