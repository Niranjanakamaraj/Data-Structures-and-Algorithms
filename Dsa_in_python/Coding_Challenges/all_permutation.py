class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        nums.sort()
        def f(i):
            if i==len(nums):
                arr.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                f(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        f(0)
        return arr