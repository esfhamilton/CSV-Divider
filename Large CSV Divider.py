# Large CSV Divider
import pandas as pd

# Replace with CSV File Names (all need to be in same folder)
tags = ['dataset1', 'dataset2', 'dataset3']

# Amount of rows for each partition (1048575 is the maximum that Excel handles) 
chunksize = 1048575

# Imports 'chunksize' rows of data from each file and creates a smaller CSV file with them
for tag in tags:
    # Replace {PATH TO FOLDER} with the path to the folder containing CSV files
    for chunk in pd.read_csv('{PATH TO FOLDER}\{}'.format(tag), chunksize=chunksize):
        print('Creating {} new.csv'.format(tag))
        chunk.to_csv('{PATH TO FOLDER}\{} new.csv'.format(tag), index=False)
        print('{} new.csv has been created successfully'.format(tag))
        break 
