import os
import sys
import pandas as pd

os.chdir('data')
files = os.listdir()

def get_timestamp(filename):
    timestamp = filename[-17:-4]
    date = timestamp[:8]
    time = timestamp[9:]
    time_dict = {'0931' : 'morning',
                 '1230' : 'midday',
                 '1601' : 'evening'}
    return timestamp, date, time_dict[time]



for file in files:
    df = pd.read_csv(file)
    timestamp, date, time = get_timestamp(file)
    df['timestamp'] = timestamp
    df['date'] = date
    df['time'] = time
    
    path = '../projects/gainers/seeds/' + file
    df.to_csv(path, index=False)
