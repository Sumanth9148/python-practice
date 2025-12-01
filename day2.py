# rotate array

def rotate_array(nums: list[int], k: int) -> list[int]:
    k=k%len(nums)

    def rev(l,r):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1


    rev(0,len(nums)-1)

    rev(0,k-1)

    rev(k,len(nums)-1)

    return nums 

print(rotate_array(nums=[1,2,3,4,5,6,7], k=3))  

print(rotate_array(nums=[-1,-100,3,99], k=2))


#hi