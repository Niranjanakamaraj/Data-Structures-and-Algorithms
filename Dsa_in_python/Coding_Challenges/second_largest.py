    def getSecondLargest(self, arr):
        l1,l2=arr[0],-1
        for i in range(1,len(arr)):
            if l1<arr[i]:
                l2=l1
                l1=arr[i]
            elif (l1>arr[i] and arr[i]>l2):
                l2=arr[i]
        if l1==l2:
            return -1
        else:
            return l2