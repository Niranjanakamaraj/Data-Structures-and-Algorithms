class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        arr=[]
        for i in range(len(val)):
            x=(val[i]/wt[i])
            arr.append([val[i],wt[i],x])
        arr.sort(key=lambda x:x[2],reverse=True)
        r=capacity
        sum=0
        for i in range(len(arr)):
            if r>0:
                if r>=arr[i][1]:
                    sum+=arr[i][0]
                    r-=arr[i][1]
                else:
                    sum+=(r*arr[i][2])
                    break
        return sum