'''4. Write a Python program to read 2 string values from the user and check whether all the characters of String1 are present in String2.
Note: You should check for all characters in string1 present in string2 but no need to bother about the order in which they appear.
 


Input Format:
Line 1: <String 1 value>
Line 2: <String 2 value>
Output Format:
Print 1 -> if the string is a balanced string Print -1 -> if the string is a unbalanced string

Input:
hut hunter Output:
1

Input:
Enter String 1: program Enter String 2: programming Output:
1

Input:
Enter String 1: java Enter String 2: python Output:
-1'''
str1=input("Enter a string one:")
str2=input("Enter a string two to be searched:")
if str2 in str1:
    print("1")
else:
    print("-1")