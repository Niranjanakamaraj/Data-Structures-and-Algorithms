class Solution:
    def maxMeetings(self, s, f) :
        arr=[]
        for i in range(len(s)):
            arr.append([s[i],f[i],i+1])
        arr.sort(key=lambda x:x[1])
        e=arr[0][1]
        a=[arr[0][2]]
        for i in range(1,len(arr)):
            if arr[i][0]>e:
                a.append(arr[i][2])
                e=arr[i][1]
        return sorted(a)