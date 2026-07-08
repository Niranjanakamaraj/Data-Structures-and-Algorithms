class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        main,subset=[],[]
        def f(i):
            main.append(subset.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                subset.append(nums[j])
                f(j+1)
                subset.pop()
        f(0)
        return main