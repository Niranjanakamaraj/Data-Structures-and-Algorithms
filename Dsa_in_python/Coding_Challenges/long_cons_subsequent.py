class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        l=0
        a=set(nums)
        for i in a:
            if i-1 not in a:
                count=1
                x=i+1
                while x in a:
                    x+=1
                    count+=1
                l=max(count,l)
        return l