#!/usr/bin/env python
import pandas as pd


def read_csv(file_name):
    df = pd.read_csv(file_name)
    df = df[["GO Report Date", 'GO District']]
    df = df.rename(columns={"GO Report Date": "date", "GO District": "district"})
    df['count'] = 1
    return df


def convert_dates_to_months(df):
    df['month'] = df['date'].apply(lambda x: x.split('-')[1])
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
    df = df.drop(['date'], axis=1)
    return df


def main(file_name):
    df = read_csv(file_name)
    df = convert_dates_to_months(df)
    print(df)


if __name__ == "__main__":
    main("crimes_small.csv")
