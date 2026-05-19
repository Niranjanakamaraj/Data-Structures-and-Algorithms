class Solution(object):
    def countOppositeParity(self, nums):
        o,e=0,0
        result=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                e+=1
            else:
                o+=1
        for i in range(len(nums)):
            if nums[i]%2==0:
                e-=1
                result.append(o)
            else:
                o-=1
                result.append(e)
        return result