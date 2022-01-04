'''2. strings, s1 and s2, create a new string by appending s2 in the middle of s1

Input Format:
Line 1: <String value> Line 2: <String value> Output Format: Line 1: <resulting string>

Input: Python Java Output: pytjavahon

Input: programming java  Output:
prograjavamming

Input: Ault Kelly Output: AuKellylt'''
str1=input("Enter a string one:")
str2=input("Enter a string two:")
print(str1[:2] + str2 + str1[2:])