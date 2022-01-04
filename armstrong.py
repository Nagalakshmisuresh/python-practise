n=int(input("Enter a number"))
sum=0
temp=n
count=len(str(n))
while(n!=0):
    rem=n%10
    sum=sum+rem**count
    n=n//10
if(temp==sum):
    print("armstrong")
else:
    print("not armstrong")