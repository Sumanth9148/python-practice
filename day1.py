#two sum

# def two_sum(nums:list[int],target:int) -> list[int]:
#     prevmap={}

#     for i,num in enumerate(nums):
#         diff=target-num
#         if diff in prevmap:
#             return [prevmap[diff],i]
#         prevmap[num]=i

#     return []

# print(two_sum(nums=[2,7,11,15], target=9)) 

# print(two_sum(nums=[3,2,4], target=6)) 




#three sum

# def three_sum(nums: list[int]) -> list[list[int]]:
#     res=[]
#     nums.sort()

#     for i,num in enumerate(nums):
#         if i>0 and num==nums[i-1]:
#             continue

#         l,r=i+1,len(nums)-1

#         while l<r:
#             ts=num+nums[l]+nums[r]

#             if ts>0:
#                 r-=1
#             elif ts<0:
#                 l+=1
#             else:
#                 res.append([num,nums[l],nums[r]])
#                 l+=1
#                 while l<r and nums[l]==nums[l-1]:
#                     l+=1

#     return res

# print(three_sum(nums=[-1,0,1,2,-1,-4])) 



#valid anagram

def valid_anagram(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    
    s_count={}

    for ch in s:
        s_count[ch]=s_count.get(ch,0)+1

    #decrease that s_count now

    for ch in t:
        if ch not in s_count:
            return False

        s_count[ch]-=1

        if s_count[ch]<0:
            return False

    return True



print(valid_anagram(s="anagram", t="nagaram"))

print(valid_anagram(s="rat", t="car"))