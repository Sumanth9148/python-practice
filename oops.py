# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks


# s1=Student("sumanth",68)
# print(s1.name,s1.marks)  


# class Account:

#     def __init__(self,bal,acc_no):
#         self.bal=bal
#         self.acc_no=acc_no


#     def debit(self,amt):
#         self.bal -= amt
#         print("amount debited was",amt)
#         print("balance is",self.bal)


#     def credit(self,amt):
#         self.bal += amt
#         print("amount credited was",amt)
#         print("balance is",self.bal)

#     def get_bal(self):
#         return self.bal 


# a1=Account(10000,1234)
# a1.debit(500)
# a1.credit(1000) 


# from abc import ABC,abstractmethod
# class Pay(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
        

# class Gpay(Pay):
#     def pay(self,amount):
#         print(f"{amount} is added in Gpay")


# class Paytm(Pay):
#     def pay(self,amount):
#         print(f"{amount} is added in Paytm")


# g1=Gpay()
# g1.pay(9000)

# p2=Paytm()
# p2.pay(7000)                

# p3=Pay()
# p3.pay()


from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,brand):
        self.name=brand

    @abstractmethod
    def start(self):
        pass

    v="hii"


class BMW(Car):

    def start(self):
        print(f"{self.name} is started")


b1=BMW("BMW")
b1.start()
print(b1.v)

