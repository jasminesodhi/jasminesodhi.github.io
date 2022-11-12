import pandas as pd
import json
# read DataFrame
data = pd.read_csv("movies_with_genres.csv")
size = len(data)/2
size = int(size)
print(size)
# no of csv files with row size
k = 2

 
for i in range(k):
    df = data[size*i:size*(i+1)]
    df.to_csv(f'roles_{i+1}.csv', index=False)