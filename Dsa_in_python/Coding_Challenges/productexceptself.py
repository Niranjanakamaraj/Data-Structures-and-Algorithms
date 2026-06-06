def product_except_self(nums):
    result=[1]*len(nums)
    previous,post=1,1
    for i in range(len(nums)):
        result[i]=previous
        previous*=nums[i]
    for j in range(len(nums)-1,-1,-1):
        result[j]*=post
        post*=nums[j]
    return result