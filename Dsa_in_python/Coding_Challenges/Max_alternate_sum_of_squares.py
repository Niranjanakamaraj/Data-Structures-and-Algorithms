class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c,d,sum=0,0,0
        arr=[]
        nums.sort(key=abs)
        a=nums[0:len(nums)//2]
        b=nums[len(nums)//2:]
        for i in range(len(nums)):
            if i%2==0 and b!=[]:
                arr.append(b[c])
                c+=1
            elif i%2!=0 and a!=[]:
                arr.append(a[d])
                d+=1
        for i in range(len(arr)):
            if i%2==0:
                sum+=arr[i]*arr[i]
            else:
                sum-=arr[i]*arr[i]
        return sum