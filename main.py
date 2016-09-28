#!/usr/bin/env python
import pandas as pd


def read_csv(file_name):
    df = pd.read_csv(file_name)
    rename_dict = {"GO Report Date": "date", "GO District": "district"}
    df = df.rename(columns=rename_dict)[list(rename_dict.values())]
    df['count'] = 1.0
    return df


def convert_date_to_month(df):
    df = df.copy()
    df['month'] = df['date'].apply(lambda x: x.split('-')[1])
    return df


def main(file_name):
    df = read_csv(file_name)
    df = convert_date_to_month(df)
    print(df)


if __name__ == "__main__":
    main('crimes_small.csv')
