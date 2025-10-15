class Solution: 
    def selectionSort(self, arr):
        n=len(arr)
        for i in range(n):
            min=i
            for j in range(i,n):
                if arr[min]>arr[j]:
                    min=j
            arr[min],arr[i]=arr[i],arr[min]