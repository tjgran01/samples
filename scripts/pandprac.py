import pandas as pd
import os

def main():

    data_dir = "../data/"

    for fname in os.listdir(data_dir):
        print(fname)
        df = pd.read_csv(f"{data_dir}{fname}")
        for col in df.columns:
            print(f"The mean value for {col} - {df[col].mean()}")

if __name__ == "__main__":
    main()
