a=input("enter string:")
sum=0
count=0
for cha in a:
    if cha.isdigit():
        sum=sum+int(cha)
        count=count+1
print("sum is:",sum)
print("average is:",(sum/count))