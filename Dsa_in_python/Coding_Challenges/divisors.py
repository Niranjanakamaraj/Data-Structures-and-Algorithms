def div(n):
    for i in range(n+1):
        if (i!=0 and n%i==0):
            print(i,end=" ")
n=int(input("Enter a number:"))
print("The divisors of",n,"are:",end=" ")
div(n)