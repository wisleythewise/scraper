import pandas as pd 
import numpy as np 
import re

check = np.array([['MAYVES', 'x', 'x', 'x', 'x'], ['LAGARDZ fragrances', 'https://instagram.com/lagardzfragrances', '6.5 K', 'x', 'x'], ['Het Muizenhuis', 'https://instagram.com/hetmuizenhuis', '19.6 K', 'x', 'x']])

df = pd.DataFrame()

df["brandname"] = check[:,0]
df["instagram"] = check[:,1]

print(df)