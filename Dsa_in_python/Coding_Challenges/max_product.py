class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return nums[0]
        p,s,m1,m2=1,1,0,0
        for i in range(len(nums)):
            if nums[i]!=0:
                p*=nums[i]
                m1=max(p,m1)
            elif nums[i]==0:
                p=1
                m1=max(0,m1)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=0:
                s*=nums[i]
                m2=max(s,m2)
            elif nums[i]==0:
                s=1
                m2=max(0,m2)
        return max(m1,m2)