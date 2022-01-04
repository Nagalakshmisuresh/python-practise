def primenumbers(n):
    count=0
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                count=count+1
    if count==0:
        print("prime number")
    else:
        print("not prime number")
n=int(input())
primenumbers(n)