class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        s=[]
        j=0
        for i in range(1,n+1):
            if len(target)>j:
                if i==target[j]:
                    s.append("Push")
                    j+=1
                else:
                    s.append("Push")
                    s.append("Pop")
        return s