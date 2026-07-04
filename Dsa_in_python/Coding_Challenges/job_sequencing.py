class Solution:
    def jobSequencing(self, deadline, profit):
        count,sum,m=0,0,max(deadline)
        arr,time=[],[]
        for i in range(m):
            time.append(0)
        for i in range(len(deadline)):
            arr.append([deadline[i],profit[i]])
        arr.sort(key=lambda x:x[1],reverse=True)
        
        for i in range(len(arr)):
            for j in range(arr[i][0]-1,-1,-1):
                if time[j]==0:
                    time[j]=arr[i][1]
                    sum+=arr[i][1]
                    count+=1
                    break
        return [count,sum]