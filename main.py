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
    df['date'] = pd.to_datetime(df['date'], format="%d-%b-%y")
    df['month'] = df['date'].dt.month
    return df


def get_monthly_counts(df):
    df = df.groupby(['month'], as_index=False)['count'].sum()
    df = df.rename(columns=dict(count='monthly_count'))
    return df


def get_monthly_counts_by_district(df):
    df = df.groupby(['month', 'district'], as_index=False)['count'].sum()
    return df


def get_monthly_demand_index_by_district(df):
    monthly_counts = get_monthly_counts(df)
    df = get_monthly_counts_by_district(df)
    df = df.merge(monthly_counts, on='month')
    df['demand_index'] = df['count'] / df['monthly_count']
    df = df.drop(['count', 'monthly_count'], axis=1)
    return df


def convert_month_to_string(df):
    df['month'] = pd.to_datetime(df['month'], format='%m').dt.strftime('%b')
    return df


def main(file_name):
    df = read_csv(file_name)
    df = convert_date_to_month(df)
    df = get_monthly_demand_index_by_district(df)
    df = convert_month_to_string(df)
    return df


if __name__ == "__main__":
    print(main('crimes.csv'))
