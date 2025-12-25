count,max=1,1
        if len(nums)<2:
            return len(nums)
        nums.sort()
        last_small=nums[0]
        for i in range(1,len(nums)):
            if nums[i] == last_small+1:
                count+=1
                last_small=nums[i]
                if count>max:
                    max=count
            elif nums[i]==last_small:
                continue
            elif nums[i]!=last_small+1:
                count=1
                last_small=nums[i]
        return max