import sys
sys.path.append('.')

import bin.normalize_csv
import pandas as pd

def test_df():
    df = bin.normalize_csv.read_gainers('ygainers.csv')
    assert isinstance(df, pd.DataFrame), f'read_gainers failed to return a DataFrame: {type(df)}'

def test_headers():
    df = bin.normalize_csv.read_gainers('ygainers.csv')
    assert (df.columns == ['symbol', 'price', 'price_change', 'price_percent_change']).all(), f'read_gainers returned df with wrong headers: {df.columns}'

def test_concat():
    df1 = bin.normalize_csv.read_gainers('wsjgainers.csv')
    df2 = bin.normalize_csv.read_gainers('ygainers.csv')
    num_columns = 4
    num_rows = df1.shape[1] + df2.shape[1]

    assert pd.concat([df1, df2]).shape == (num_rows, num_columns), 'read_gainers returned uncompatible dataframes'


