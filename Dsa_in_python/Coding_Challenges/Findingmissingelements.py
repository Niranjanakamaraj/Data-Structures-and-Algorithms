class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n=[]
        for i in range(len(nums)):
            if nums[i-1]+1!=nums[i]:
                 n.extend(range(nums[i-1]+1,nums[i]))
        return n