intervals.sort()
        if len(intervals)<=1:
            return intervals
        arr=[]
        cur=intervals[0]
        for i in range(1,len(intervals)):
            if cur[1]>=intervals[i][0]:
                cur[1]=max(cur[1],intervals[i][1])
            else:
                arr.append(cur)
                cur=intervals[i]
        arr.append(cur)
        return arr