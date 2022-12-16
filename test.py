import pandas as pd
from sklearn.model_selection import train_test_split
from normscaler.scaler import DecimalScaler

# read data
url = 'https://raw.githubusercontent.com/shoukewei/data/main/data-pydm/gdp_china_encoded.csv'
df = pd.read_csv(url)

# slice data to feature X and Target y
X = df.drop(['gdp'],axis=1)
y = df['gdp']

# split date gor training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.30, random_state=1)

# call the DecimalScaler
X_train_scaled, X_test_scaled = DecimalScaler(X_train,X_test)

# display normalized training data
X_train_scaled