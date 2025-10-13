class Solution:
    def getMinMax(self, arr):
        min=arr[0]
        max=arr[len(arr)-1]
        for i in arr:
            if i<min:
                min=i
            if i>max:
                max=i
        return [min,max]