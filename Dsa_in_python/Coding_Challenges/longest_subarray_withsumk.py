class Solution:
    def longestSubarray(self, arr, k):  
        sum,count=0,0
        dic={0:1}
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==k:
                count=i+1
            
            if sum-k in dic:
                length=i-dic[sum-k]
                if length>count:
                    count=length
            if sum not in dic:
                dic[sum]=i
        return count