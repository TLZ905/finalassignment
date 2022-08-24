import numpy as np
import pandas as pd

input = ['Iris-setosa','Iris-versicolor','Iris-virginica']
num = np.array(input)
reshaped = num.reshape(3,1)
pd.DataFrame(reshaped, columns=['Species'])