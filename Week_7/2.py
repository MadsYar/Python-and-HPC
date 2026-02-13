from pyarrow import csv
import pyarrow as pa
import pandas as pd
import time

def pyarrow_load(fname):

    start = time.time()
    arrow_table = csv.read_csv(fname)
    end = time.time()
    return arrow_table