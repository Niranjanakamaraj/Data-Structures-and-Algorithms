count,m=0,0
for i in range(1,len(nums)):
    if nums[i]<=nums[i-1]:
        count=i
    else:
        continue