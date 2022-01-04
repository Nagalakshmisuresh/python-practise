#1.Write a program to read a number from the user and print its equivalent
#Binary, Octal, and Hexadecimal values
#Input:
#Enter the Number: 100
#Output:
#Binary Equivalent of 100 is 0b1100100
#Octal Equivalent of 100 is 0o144
#Hexadecimal Equivalent of 100 is 0x64
a=int(input("Enter a number"))
print(bin(a))
print(oct(a))
print(hex(a))