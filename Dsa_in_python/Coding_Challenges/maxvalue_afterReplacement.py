class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        nums.sort(key=abs)
        nums=nums[len(nums)-2:len(nums)]
        m=nums[0]*nums[1]
        if m<1:
            m*=-100000
        else:
            m*=100000
        return m