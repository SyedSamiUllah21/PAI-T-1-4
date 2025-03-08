import pandas as pd
from sklearn.ensemble import RandomForestRegressor

home_data_file_path = (r'C:\Users\Sami\Downloads\train.csv')
home_data = pd.read_csv(home_data_file_path)

y = y = home_data.SalePrice

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'FullBath',
            'HalfBath','BedroomAbvGr', 'KitchenAbvGr', 'Fireplaces', 'PoolArea', 
            'TotRmsAbvGrd']
X = home_data[features]

home_model = RandomForestRegressor(random_state=0)
home_model.fit(X, y)

test_data_path = (r'C:\Users\Sami\Downloads\test.csv')
test_data = pd.read_csv(test_data_path)

test_X = test_data[features]

test_preds = home_model.predict(test_X)


output = pd.DataFrame({'Id': test_data.Id, 'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)


