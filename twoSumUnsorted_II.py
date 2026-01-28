from typing import List
def twoSum( nums: List[int], target: int) -> List[int]:
    n=len(nums)
    dict={}
    
    for i in range(n):
        rem=target-nums[i]
        if rem in dict:
            return[dict[rem],i]
        else:
            dict[nums[i]]=i

nums = [3,2,4]
target=6
print(twoSum(nums,target))
