import sys
import pandas as pd

def total_precip(df):
    total = 0.0
    for i in range(len(df)):
        row = df.iloc[i]
        if row['parameterId'] == 'precip_past10min':
            total += row['value']
    return total

if __name__ == "__main__":
    
    csv_path = sys.argv[1]

    df = pd.read_csv(csv_path)

    total = total_precip(df)

    print(total)