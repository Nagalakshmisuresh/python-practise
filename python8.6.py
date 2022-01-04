'''5. Write a Python program to read the given below string, and print the sum and average of the digits that appear in the string, ignoring all 
other characters.
String = "English=78 Science=83 Math=68 History=65"

Input Format:
Line 1: <String 1 value>
Output Format:
<Numbers present in the given string – print each value in a separate line>
<sum value>
<average value>

Input:
English=78 Science=83 Math=68 History=65
Output:
78
83
68
65
294
58.8'''
st = "English=78 Science=83 Math=68 History=65"
sum=0
for i in range(len(st)):
    if  st[i] >= '0' and st[i] <= '9':
        print(st[i]+st[i+1])
        sum=sum+eval(st[i]+st[i+1])
        avg=sum/4
print(sum)
print(avg)