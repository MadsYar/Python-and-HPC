import sys
import pandas as pd
import time
import pyarrow as pa
import pyarrow.parquet as pq
import os
from pyarrow import csv

def pyarrow_load(fname):
    
    arrow_table = csv.read_csv(fname)

    pandas_df = arrow_table.to_pandas()
   
    return pandas_df
