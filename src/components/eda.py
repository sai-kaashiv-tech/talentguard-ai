import pandas as pd

def basic_eda(data:pd.DataFrame):
    print('\n'+'='*60)
    print('Exploratory Data Analysis'.center(60))
    print('='*60)

    print(f'\nDataset Shape: {data.shape}')

    print('\nTarget Variable Distribution')
    print(data['Attrition'].value_counts())

    print('\nNumerical Variable Distribution')
    print(data.describe())

    print('\nDepartment Variable Distribution')
    print(data['Department'].value_counts())

    print(pd.crosstab(data['OverTime'], data['Attrition']))

def main():
    from data_ingestion import load_data

    data = load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()


