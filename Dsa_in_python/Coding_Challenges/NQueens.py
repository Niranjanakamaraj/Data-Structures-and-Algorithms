class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n) ]
        sol=[]

        c=n*[False]
        d1=(2*n-1)*[False]
        d2=(2*n-1)*[False]

        def f(i):
            if i==n:
                sol.append(["".join(r) for r in board])
                return

            for j in range(n):
                if c[j] or d1[i-j+n-1] or d2[i+j]:
                    continue
                
                board[i][j]='Q'
                c[j]=True
                d1[i-j+n-1]=True
                d2[i+j]=True

                f(i+1)

                board[i][j]='.'
                c[j]=False
                d1[i-j+n-1]=False
                d2[i+j]=False

        f(0)
        return sol