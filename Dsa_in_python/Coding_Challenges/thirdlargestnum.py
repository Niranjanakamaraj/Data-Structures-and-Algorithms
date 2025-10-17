class Solution:
    def thirdLargest(self,arr):
        a=b=c=-1
        for i in range(len(arr)):
            if arr[i]>=a:
                c=b
                b=a
                a=arr[i]
            elif arr[i]>=b:
                c=b
                b=arr[i]
            elif arr[i]>=c:
                c=arr[i]
        return c