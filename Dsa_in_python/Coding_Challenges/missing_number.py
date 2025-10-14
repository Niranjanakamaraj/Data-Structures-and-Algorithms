class Solution:
    def missingNum(self, arr):
        arr.sort()
        i=0
        j=1
        if arr[0]!=1:
            return 1
        while len(arr)>j:
            if arr[i]+1 !=arr[j]:
                return arr[i]+1
            elif arr[i]+1 == arr[j]:
                i+=1
                j+=1
        return len(arr)+1