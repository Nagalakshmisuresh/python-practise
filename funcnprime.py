def primeInRange(num1,num2):
    for i in range(num1,num2):
        count=0
        for j in range(1,i):
            if i%j==0:
                count+=1
        if count<=1:
            print(i,end=' ')
primeInRange(1,100)