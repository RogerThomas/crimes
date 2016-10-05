#!/usr/bin/env python
import pandas as pd


def read_csv(file_name):
    df = pd.read_csv(file_name)
    df = df[["GO Report Date", 'GO District']]
    df = df.rename(columns={"GO Report Date": "date", "GO District": "district"})
    df['count'] = 1.0
    return df


def convert_dates_to_months(df):
    df['month'] = df['date'].apply(lambda x: x.split('-')[1])
    df = df.drop(['date'], axis=1)
    return df


def get_monthly_counts_by_district(df):
    df = df.groupby(['month', 'district'], as_index=False)['count'].sum()
    return df


def get_monthly_demand_index_by_district(df):
    monthly_counts = df.groupby('month', as_index=False)['count'].sum()
    monthly_counts = monthly_counts.rename(columns=dict(count='monthly_count'))
    df = df.merge(monthly_counts, on='month')
    df['demand_index'] = df['count'] / df['monthly_count']
    df = df.drop(['count', 'monthly_count'], axis=1)
    return df


def sort_df_by_month_demand_index_and_district(df):
    month_number_map = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    df['month_number'] = df['month'].map(month_number_map)
    df = df.sort_values(["month_number", "demand_index", "district"], ascending=True)
    df = df.drop('month_number', axis=1)
    df = df.reset_index(drop=True)
    return df


def main(file_name):
    df = read_csv(file_name)
    df = convert_dates_to_months(df)
    df = get_monthly_counts_by_district(df)
    df = get_monthly_demand_index_by_district(df)
    df = sort_df_by_month_demand_index_and_district(df)
    return df


if __name__ == "__main__":
    df = main("crimes.csv")
    df.to_csv('results.csv', index=False)
    print(df)
