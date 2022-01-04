'''3.Write a Python program to count all the Lowercase, Uppercase, Digits and Special symbols from a given string.

Input Format:
Line 1: <String value>
Output Format:
Line 1: <Number of uppercase characters> Line 2: <Number of lowercase characters> Line 3: <Number of digits characters>
Line 4: <Number of special symbols characters>

Input: Anushya.1083@gmail.com Output:
1
14
4
3

Input:
 

1083
Output:
0
0
0'''
st=input("Enter a string :")
uc=0
lc=0
nc=0
sc=0
for i in range(len(st)):
          if st[i] >= 'A' and st[i] <= 'Z':
              uc=uc+1
              
          elif st[i] >= 'a' and st[i] <= 'z':
              lc=lc+1
          elif st[i] >= '0' and st[i] <= '9':
              nc=nc+1
          else:
              sc=sc+1
print(uc)
print(lc)
print(nc)
print(sc)