class Solution:
    def insertionSort(self, arr):
        for i in range(1,len(arr)):
            j=i-1
            cur=arr[i]
            while j>=0 and cur<arr[j]:
                arr[j+1]=arr[j]
                j-=1
                arr[j+1]=cur
        return arr