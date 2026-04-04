def movezeros(self,nums):
    l=0
    for r in range(l+1,len(nums):
        if nums[l]==0 and nums[r]!=0:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
        elif nums[l]!=0:
            l+=1
    return nums