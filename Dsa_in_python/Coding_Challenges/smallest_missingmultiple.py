class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        large=nums[len(nums)-1]
        i=1
        while i<=(large//k)+1 :
            m=k*i
            if m not in nums:
                return m
            i+=1