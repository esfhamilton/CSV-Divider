import os
import pandas as pd
from pandas import DataFrame

# Trim CSV files with more than 1048575 rows  
def trim_csv():
    # CSV file names in target folder
    csvs = os.listdir('[PATH CONTAINING CSVS]')

    # Remove none .csv files
    csvs = [csv for csv in csvs if '.csv' in csv]
    
    # Amount of rows for each partition (1048575 is the maximum that Excel handles) 
    chunksize = 1048575

    # Imports 'chunksize' rows of data from each file and creates a smaller CSV file with them 
    for csv in csvs:
        for chunk in pd.read_csv('[PATH CONTAINING CSVS]\\{}'.format(csv),dtype='unicode',chunksize=chunksize):
            print('Creating Trimmed {}'.format(csv))
            chunk.to_csv('[PATH CONTAINING CSVS]\\Trimmed {}'.format(csv), index=False)
            print('Trimmed {} has been created successfully'.format(csv))
            break 

# Separates each class into new individual csv files
def class_separator():
    csvs = os.listdir('[PATH CONTAINING CSVS]')

    # Remove none csv files
    csvs = [csv for csv in csvs if '.csv' in csv]
    
    for csvIndex, csv in enumerate(csvs):        
        df = pd.read_csv('[PATH CONTAINING CSVS]\\{}'.format(csv),sep='\s*,\s*',engine='python',dtype='unicode')
        print("Separating Classes")
        labels = []
        newDatasets = {}

        for i, row in enumerate(df.iterrows()):
            if(i%10000==0 and i>0):
                print(str(i)+' rows processed')
                
            # Add data from row to corresponding list
            tempList = []
            for i in range(len(row[1])):
                tempList.append(row[1][i])
                
            # Initialise a new list for each distinct label     
            if(row[1]['Label'] not in labels):
                labels.append(row[1]['Label'])
                newDatasets[row[1]['Label']] = []
                
            newDatasets[row[1]['Label']].append(tempList)

        # Create new directory to store decomposed class files
        os.mkdir('[PATH CONTAINING CSVS]\\{}'.format(csvs[csvIndex].strip('.csv') + ' Decomposition'))
        for label in labels:
            newDataset = DataFrame(newDatasets[label], columns=df.columns)
            # Replace Test1 with Name of original dataset + Decomposition
            newDataset.to_csv('[PATH CONTAINING CSVS]\\{}\\{}.csv'.format(csvs[csvIndex].strip('.csv')+ ' Decomposition',label), index=False)
             
#trim_csv()
#class_separator()
