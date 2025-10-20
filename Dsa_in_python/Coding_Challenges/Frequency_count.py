class Solution:
    def frequencyCount(self, arr):
        d={i:0 for i in range(1,len(arr)+1)}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(1,len(arr)+1):
            if i not in d:
                d[i]=0
        return list(d.values())