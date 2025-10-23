class Solution:
    def findTriplets(self, arr):
        n=len(arr)-1
        arr.sort()
        for i in range(n):
            j=n
            k=i+1
            while k<j:
                sum=arr[i]+arr[j]+arr[k]
                if sum==0:
                    return True
                elif sum<0:
                    k+=1
                else:
                    j-=1
        return False