def sorted(nums):
    iv=0
    if nums[-1]<nums[0]:
        iv=1
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            iv+=1
            if iv>1:
                return False
    return True