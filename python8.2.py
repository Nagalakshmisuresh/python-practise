'''1.Given a string of odd length greater than or equal to 7, return a string made of the middle three chars of a given String. And if the string 
length is less than 7, return the original string value itself as the output.
 Input Format: Line 1: 
Output Format: Line 1:
 Input: JhonDipPeta 
Output: Dip 
Input: JaSonAy
 Output: Son 
Input: Anushya 
Output: Original String is: Anushya Middle three chars: ush
 Input: Programming
 Output: Original String is: Programming Middle three chars: ram''' 
str=input("Enter the string: ")
l=len(str)
if l>=7:
    if l%2!=0:
        l1=l//2
        print(str[l1-1:l1+2])
    else:
        print("not sufficient")
else:
    print("not suitable")
 