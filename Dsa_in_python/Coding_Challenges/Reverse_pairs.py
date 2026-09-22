self.count = 0
        l,r=0,len(nums)-1
        def mergesort(nums,l,r):
            if l>=r:
                return
            m=(l+r)//2
            mergesort(nums,l,m)
            mergesort(nums,m+1,r)
            merge(nums,l,m,r)
        def merge(nums,l,m,r):
            left=nums[l:m+1]
            right=nums[m+1:r+1]
            i,j,k=0,0,l
            b=0
            for a in range(len(left)):
                while b<len(right) and left[a]>right[b]*2:
                    b+=1
                self.count+=b
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
        mergesort(nums,l,r)
        return self.count