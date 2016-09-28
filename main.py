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


def get_monthly_counts(df):
    df = df.groupby(['month'], as_index=False)['count'].sum()
    return df


def get_monthly_counts_by_district(df):
    df = df.groupby(['month', 'district'], as_index=False)['count'].sum()
    return df


def main(file_name):
    df = read_csv(file_name)
    df = convert_date_to_month(df)
    monthly_counts = get_monthly_counts(df)
    df = get_monthly_counts_by_district(df)
    print(monthly_counts)


if __name__ == "__main__":
    main('crimes_small.csv')
