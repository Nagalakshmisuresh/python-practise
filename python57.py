#Program to find the position of minimum and maximum elements of a list.
list=[23,45,67,92,88]
min_ele,max_ele=list[0],list[0]
for i in range(1,len(list)):
    if list[i]<min_ele:
        min_ele=list[i]
    if list[i]>max_ele:
        max_ele=list[i]
print("minimum element: ",min_ele)
print("maximum element: ",max_ele)




