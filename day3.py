#longest consecutive sequence

def longest_consecutive_sequence(nums: list[int]) -> int:
    numset=set(nums)
    longest=0

    for num in nums:
        if (num-1) not in numset:
            len=0
            while (num+len) in numset:
                len+=1

            longest=max(len,longest)
    return longest 


print(longest_consecutive_sequence(nums=[100, 4, 200, 1, 3, 2]))


#trapping rain water

def trapping_rain_water(height: list[int]) -> int:
    n=len(height)

    lm=[0]*n
    rm=[0]*n
    ans=0

    lm[0]=height[0]
    for i in range(1,n):
        lm[i]=max(lm[i-1],height[i])

    rm[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        rm[i]=max(rm[i+1],height[i])

    for i in range(n):
        ans+=min(lm[i],rm[i])-height[i]

    return ans

print(trapping_rain_water(height=[0,1,0,2,1,0,1,3,2,1,2,1]))            

