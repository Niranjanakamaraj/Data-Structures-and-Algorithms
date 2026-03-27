dict={}
        for i,v in enumerate(nums):
            n=target-v
            if n in dict:
                return[dict[n],i]
            dict[v]=i