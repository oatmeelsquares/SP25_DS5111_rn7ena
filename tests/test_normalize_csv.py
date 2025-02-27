''' This module tests the functionality of bin.normalize_csv.py
    
    Author: rn7ena@virginia.edu
'''

import sys
import pandas as pd
sys.path.append('.')

import bin.normalize_csv

def test_df():
    ''' make sure read_gainers returns a pandas dataframe'''
    df = bin.normalize_csv.read_gainers('ygainers.csv')
    assert isinstance(df, pd.DataFrame), f'read_gainers failed to return a DataFrame: {type(df)}'

def test_headers():
    ''' make sure read_gainers returns a df with the correct headers'''
    headers = ['symbol', 'price', 'price_change', 'price_percent_change']
    df = bin.normalize_csv.read_gainers('ygainers.csv')
    assert (df.columns == headers).all(), f'returned df with wrong headers: {df.columns}'

def test_concat():
    ''' make sure read_gainers returns dfs that can be
        easily merged with the correct dimensions'''
    df1 = bin.normalize_csv.read_gainers('wsjgainers.csv')
    df2 = bin.normalize_csv.read_gainers('ygainers.csv')
    num_rows = df1.shape[0] + df2.shape[0]
    right_shape = (num_rows, 4)
    df = pd.concat([df1, df2], axis = 0)

    assert df.shape == right_shape, f'read_gainers returned uncompatible dataframes {str(df)}'
