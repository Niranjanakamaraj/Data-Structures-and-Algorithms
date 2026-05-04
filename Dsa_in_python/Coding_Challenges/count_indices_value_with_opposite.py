class Solution(object):
    def countOppositeParity(self, nums):
        odd,even=0,0
        result=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even+=1
            else:
                odd+=1
        for i in range(len(nums)):
            if nums[i]%2==0:
                even-=1
                result.append(odd)
            else:
                odd-=1
                result.append(even)
        return result