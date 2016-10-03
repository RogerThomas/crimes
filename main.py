#!/usr/bin/env python
import pandas as pd

def read_csv(file_name):
    df = pd.read_csv(file_name)
    df = df[['GO Report Date', 'GO District']]
    df = df.rename(
        columns={"GO Report Date": 'date', "GO District": 'district'}
    )
    df['count'] = 1
    return df


def count_crimes_by_month_and_district(df):
    df['month'] = df['date'].apply(lambda x: x.split('-')[1])
    df = df.groupby(["month", "district"], as_index=False)['count'].sum()
    return df


def get_demand_index_per_month_and_district(df):
    return df


def main(file_name):
    df = read_csv(file_name)
    df = count_crimes_by_month_and_district(df)
    return df


if __name__ == "__main__":
    result = main("crimes_small.csv")
    print(result)
