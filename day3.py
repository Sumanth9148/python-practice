#longest consecutive sequence

# def longest_consecutive_sequence(nums: list[int]) -> int:
#     numset=set(nums)
#     longest=0

#     for num in nums:
#         if (num-1) not in numset:
#             len=0
#             while (num+len) in numset:
#                 len+=1

#             longest=max(len,longest)
#     return longest 


# print(longest_consecutive_sequence(nums=[100, 4, 200, 1, 3, 2]))




#trapping rain water

# def trapping_rain_water(height: list[int]) -> int:
#     n=len(height)

#     lm=[0]*n
#     rm=[0]*n
#     ans=0

#     lm[0]=height[0]
#     for i in range(1,n):
#         lm[i]=max(lm[i-1],height[i])

#     rm[n-1]=height[n-1]
#     for i in range(n-2,-1,-1):
#         rm[i]=max(rm[i+1],height[i])

#     for i in range(n):
#         ans+=min(lm[i],rm[i])-height[i]

#     return ans

# print(trapping_rain_water(height=[0,1,0,2,1,0,1,3,2,1,2,1]))     

# print(trapping_rain_water(height=[4,2,0,3,2,5]))




#container with most water

def container_with_most_water(height: list[int]) -> int:
    l=0
    r=len(height)-1
    max_area=0

    while l<r:
        w=r-l
        h=min(height[l],height[r])
        area=w*h

        max_area=max(max_area,area)

        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return max_area

print(container_with_most_water(height=[1,8,6,2,5,4,8,3,7])) 
print(container_with_most_water(height=[1,1]))


#merged intervals
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    intervals.sort(key= lambda x:x[0])

    merged=[]
    curr_inter=intervals[0]

    for next_inter in intervals[1:]:
        if next_inter[0]<=curr_inter[1]:
            curr_inter[1]=max(next_inter[0],curr_inter[1])
        else:
            merged.append(curr_inter)
            curr_inter=next_inter
    merged.append(curr_inter)
    return merged

print(merge_intervals(intervals=[[1,3],[2,6],[8,10],[15,18]]))        