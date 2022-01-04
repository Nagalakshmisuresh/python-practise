import numpy as np
arr=np.array([1,2,3,4,5])
newarr=arr.view()
arr[1]=90
print(arr)
print(newarr)