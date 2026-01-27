nums=[0,0,1,1,1,2,2,3,3,4]
n=len(nums)
k=n
for i in range(n-1):
    if nums[i]==nums[i+1]:
        k-=1

print(k)
