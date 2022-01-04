n=int(input("Enter a number"))
count=0
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            count=count+1
if(count==0):
    print("prime numbers")
else:
    print("not prime numbers")