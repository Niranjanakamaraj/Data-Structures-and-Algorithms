        o,e=1,0
        art=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                art[e]=nums[i]
                e+=2
            else:
                art[o]=nums[i]
                o+=2
        return art