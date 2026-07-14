import pandas as pd
from config.paths import DATA_PATH

def load_data():
    '''
    Loads data from csv file
    :return: a pandas dataframe
    '''
    data = pd.read_csv(DATA_PATH/'Employee-Attrition.csv')
    return data

if __name__ == '__main__':
    data = load_data()
    print('Top 5 values')
    print(data.head(),'\n','_'*30)
    print('Row and column count')
    print(data.shape,'\n','_'*30)
    print('Column names')
    print(data.columns,'\n','_'*30)
