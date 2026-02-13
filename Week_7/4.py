import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import sys
    
if __name__ == "__main__":

    csv_path = sys.argv[1]

    df = pd.read_csv(csv_path)

    parquet_path = csv_path.replace(".csv", ".parquet")

    df.to_parquet(parquet_path, engine="pyarrow", index=False)
