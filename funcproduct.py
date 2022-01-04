def product(n):
    product=1
    while(n!=0):
        rem=n%10
        product=product*rem
        n=n//10
    print(product)
product(1234)