# rotate array

# def rotate_array(nums: list[int], k: int) -> list[int]:
#     n=len(nums)
#     k=k%n

#     def rev(l,r):
#         while l<r:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
#             r-=1

#     rev(0,n-1)

#     rev(0,k-1)

#     rev(k,n-1)

#     return nums        
  

# print(rotate_array(nums=[1,2,3,4,5,6,7], k=3))  

# print(rotate_array(nums=[-1,-100,3,99], k=2))


#add two numbers

# def add_two_numbers(l1: list[int], l2: list[int]) -> list[int]:
#     res=[]
#     i=0
#     j=0
#     carry=0

#     while i<len(l1) or j<len(l2) or carry:
#         x=l1[i] if i<len(l1) else 0
#         y=l2[j] if j<len(l2) else 0

#         tot=x+y+carry
#         res.append(tot%10)
#         carry=tot//10

#         i+=1
#         j+=1
#     return res 

# print(add_two_numbers(l1=[2,4,3], l2=[5,6,4]))  


#kth largest element

def kth_largest_element_in_an_array(nums: list[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k-1]

print(kth_largest_element_in_an_array(nums=[3,2,1,5,6,4], k=2)) 
print(kth_largest_element_in_an_array(nums=[3,2,3,1,2,4,5,5,6],k=4)) 
