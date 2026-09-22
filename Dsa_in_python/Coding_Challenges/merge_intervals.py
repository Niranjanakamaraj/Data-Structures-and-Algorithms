        intervals.sort()
        a=[]
        for i in range(len(intervals)-1):
            b=intervals[i]
            c=intervals[i+1]
            if c[0]<=b[0] and c[0]>b[0]:
                a.append([b[0],c[1]])
            elif b[0]<b[1]<c[0]<c[1]:
                a.append([b,c])
        return a