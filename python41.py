#Ross next task after tables is to learn the squares and cubes.
#His teacher has explained to him that a square of a number is the product of the number by itself. And the cube of the number is the 
#product of 3 numbers which are the same. Ross has to know the Square and Cube of numbers from 1 to 10.
#Print a table for him so that he can study them easily.

#Expected Output:
#Number	Square	Cube
#1	1	1
#2	4	8
#3	9	27
#4	16	44
#5	25	152
#6	36	216
#7	49	343
#8	64	512
#9	81	729
#10	100	1000
n=int(input("Enter n value"))
i=1
print("Number square cube")
while(i<=n):
    square=i*i
    cube=i*i*i
    print(i,' ',square,' ',cube)
    i=i+1




