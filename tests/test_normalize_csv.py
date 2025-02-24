import sys
sys.path.append('.')

import bin.normalize_csv
import pandas as pd

def test_normalize_csv():
    df = bin.normalize_csv.read_gainers('ygainers.csv')
    assert isinstance(df, pd.DataFrame), f'read_gainers failed to return a DataFrame: {type(df)}'
