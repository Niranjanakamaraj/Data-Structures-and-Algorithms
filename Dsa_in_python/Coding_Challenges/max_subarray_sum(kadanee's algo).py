large,sum=nums[0],nums[0]
for i in range(1,len(nums)):
    sum = max(nums[i], sum + nums[i])
    if large<sum:
        arge=sum
return large