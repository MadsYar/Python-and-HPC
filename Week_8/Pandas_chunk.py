import pandas as pd
import sys

path = sys.argv[1]
chunk = int(sys.argv[2])

df = pd.read_csv(path, chunksize=chunk)

total_precipitation = 0

for chunk in df:
    total_precipitation += chunk.loc[chunk['parameterId'] == 'precip_past10min', 'value'].sum()

print(total_precipitation)