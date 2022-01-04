#Write a Python program to solve the Quadratic Equation
#Formula:
#ax2 + bx + c = 0, where
#a, b and c are real numbers and
#a ≠ 0
a=float(input("Enter first number"))
b=float(input("Enter second number"))
c=float(input("Enter third number"))
d=(b**2)-4*a*c
s1=(-b+(d**0.5))/(2*a)
s2=(-b-(d**0.5))/(2*a)
print(s1,s2)




