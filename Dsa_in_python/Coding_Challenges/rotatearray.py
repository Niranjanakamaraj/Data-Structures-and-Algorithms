def rotate(nums,k):
    k%=len(nums)
    nums[:]=nums[-k:]+nums[:-k]
    return nums