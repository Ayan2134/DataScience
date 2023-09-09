import numpy as np
import math
import pandas as pd
data=pd.DataFrame({"name" : ['ayan','manya','bhav','polu'] , "age" : [19,18,17,10]})
print(data)
new_data=data.copy()
arr=[4,7,6,8,4]
arr2=np.array([5,7,4,2,9])
arr=np.array(arr)
np.random.shuffle(arr)
print((new_data).shape[0])
print(arr)
print(math.e**arr)
print(1/(1+math.e**(-1*arr)))
print(arr)
print((arr>5).astype(int))
print(arr)
print(arr2.shape[0])
print((arr==arr2).astype(int))