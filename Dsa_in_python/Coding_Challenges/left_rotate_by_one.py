    def rotateArr(self, arr, d):
        temp=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[len(arr)-1]=temp
        return arr