minimum=nums[0]
profit=0
for i in range(1,len(nums):
    minimum=min(minimum,nums[i])
    profit=max(profit,nums[i]-minimum)
return profit