k=k%len(nums)
def rev(a,b):
    while a<b:
        nums[a],nums[b]=nums[b],nums[a]
        a,b=a+1,b-1
rev(0,len(nums)-1)
rev(0,k-1)
rev(k,len(nums)-1)