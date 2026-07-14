import pandas as pd

def select_features(data:pd.DataFrame):
    data = data.drop(columns=['EmployeeNumber'])

    X = data.drop(columns=['Attrition'])
    y = data['Attrition']

    return X, y

def main():
    from config.paths import DATA_PATH
    from components.data_ingestion import load_data


    data = pd.read_csv(DATA_PATH / 'Employee-Attrition.csv')
    X, y = select_features(data)
    print(X.shape)
    print(y.shape)

if __name__ == '__main__':
    main()