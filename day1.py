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


#three sum
def three_sum(nums: list[int]) -> list[list[int]]:
    res=[]
    nums.sort()

    for i,num in enumerate(nums):
        if i>0 and num==nums[i-1]:
            continue

        l,r=i+1,len(nums)-1

        while l<r:
            ts=num+nums[l]+nums[r]

            if ts>0:
                r-=1
            elif ts<0:
                l+=1
            else:
                res.append([num,nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1

    return res

print(three_sum(nums=[-1,0,1,2,-1,-4]))               