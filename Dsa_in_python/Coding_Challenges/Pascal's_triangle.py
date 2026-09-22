Triangle=[]
for i in range(numRows):
    row=[1]*(i+1)
    for j in range(1,i):
        row[j]=Triangle[i-1][j-1]+Triangle[i-1][j]
    Triangle.append(row)  
return Triangle