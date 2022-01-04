def factors(n):
    fact=1
    for i in range(1,11):
        if(n%i==0):
            print(i)
n=int(input())
factors(n)