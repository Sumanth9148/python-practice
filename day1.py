def two_sum(nums:list[int],target:int) -> list[int]:
    prevmap={}

    for i,num in enumerate(nums):
        diff=target-num
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[num]=i

    return []

print(two_sum(nums=[2,7,11,15], target=9))    