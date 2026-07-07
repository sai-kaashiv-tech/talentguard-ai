import pandas as pd
import os

Artifacts_path = "../artifacts/reports"
os.makedirs(Artifacts_path, exist_ok=True)

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
    print(str(data['Department'].value_counts()))

    print(pd.crosstab(data['OverTime'], data['Attrition']))

    with open('./artifacts/reports/dataset_summary.txt', 'w') as file:

        file.write('\n' + '=' * 60)
        file.write('\nExploratory Data Analysis'.center(60))
        file.write('\n'+'=' * 60)

        file.write(f'\nDataset Shape: {data.shape}')

        file.write('\nTarget Variable Distribution\n')
        file.write(str(data['Attrition'].value_counts()))


        file.write('\nDepartment Variable Distribution\n')
        file.write(str(data['Department'].value_counts()))

def main():
    from data_ingestion import load_data

    data = load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()


