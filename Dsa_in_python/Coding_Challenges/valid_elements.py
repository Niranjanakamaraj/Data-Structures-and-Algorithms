class Solution(object):
    def findValidElements(self, nums):
        r=[0]*len(nums)
        r[len(nums)-1]=float('-inf')
        rm=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
                r[i]=rm
                rm=max(rm,nums[i])
        res=[]
        lm=float('-inf')
        for i in range(len(nums)):
            if nums[i]>lm or nums[i]>r[i]:
                res.append(nums[i])
            lm=max(lm,nums[i])
        return res