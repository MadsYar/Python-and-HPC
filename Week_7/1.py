from pyarrow import csv
import zipfile
import time
import pandas as pd
path = "/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"

#####1

start = time.time()

with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall("/zhome/69/0/168594/Documents/HPC_course/week7")
read = pd.read_csv("2023_01.csv")
end = time.time()
print("Time with extraction: ", end - start)

start = time.time()
read = pd.read_csv(path)
end = time.time()
print("Time without extraction: ", end - start)




data = pd.read_csv("2023_01.csv")
def df_memsize (df):
    mem = df.memory_usage(index=True,deep = True).sum()
    if mem < 1024:
        print(str(mem) + " bytes")
    elif mem < 1024**2:
        print(str(mem/1024) + " kilobytes")
    elif mem < 1024**3:
        print(str(mem/(1024**2)) + " megabytes")
    else:
        print(str(mem/(1024**3)) + " gigabytes")
    return mem

def summarize_columns(df):
    print(pd.DataFrame([
        (
            c,
            df[c].dtype,
            len(df[c].unique()),
            df[c].memory_usage(deep=True) // (1024**2)
        ) for c in df.columns
    ], columns=['name', 'dtype', 'unique', 'size (MB)']))
    print('Total size:', df.memory_usage(deep=True).sum() / 1024**2, 'MB')

def reduce_dmi_df(data):
    summarize_columns(data)
    data["parameterId"] = data["parameterId"].astype("category")
    data["created"] = pd.to_datetime(data["created"], format="ISO8601")
    data["observed"] = pd.to_datetime(data["observed"], format="ISO8601")
    data["coordsx"] = data["coordsx"].astype("float32")
    data["coordsy"] = data["coordsy"].astype("float32")
    summarize_columns(data)
    return data