a=[nums[0]]
        sum=nums[0]
        suffix_min = [0] * len(nums)
        suffix_min[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i+1])
        maxi=float('-inf')
        for i in range(1,len(nums)):
            sum+=nums[i]
            a.append(sum)
        for i in range(len(a)-1):
                cur=a[i]-suffix_min[i+1]
                if cur>maxi:
                    maxi=cur
        return maxi