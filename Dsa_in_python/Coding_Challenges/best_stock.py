def maxProfit(self,profit):
    m,l=0,0
    for r in range(1,len(profit)):
        if profit[r]-profit[l]>m:
            m=profit[r]-profit[l]
        if profit[r]<profit[l]:
            l=r
        return m