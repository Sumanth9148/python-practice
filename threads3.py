#very slow

from threading import Thread

def square():
    for i in range(10**5):
        print(i*i)
        # time.sleep(0.6)


t1=Thread(target=square)
t2=Thread(target=square)

t1.start()
t2.start()


#fast for process

# from multiprocess import Process


# def square():
#     for i in range(10**5):
#         print(i*i)
        

# if __name__=="__main__":

#     t1=Process(target=square)
#     t2=Process(target=square)

#     t1.start()
#     t2.start()



