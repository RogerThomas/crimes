#!/usr/bin/env python
import pandas as pd


def read_csv(file_name):
    df = pd.read_csv(file_name)
    df = df[["GO Report Date", 'GO District']]
    df = df.rename(columns={"GO Report Date": "date", "GO District": "district"})
    df['count'] = 1
    return df


def main(file_name):
    df = read_csv(file_name)
    print(df)


if __name__ == "__main__":
    main("crimes_small.csv")
