## normscalers

A package for data normalization including the methods of *MinMaxScaler*, *MaxAbsScaler*, *RobustScaler*, *StandardScaler* and *Normalizer* in Scikit-learning, and *DecimalScaler*. The package can automatically detect the one-hot encoded variables and skip them to be normalized.

## Install 
```python
pip install normscaler
```
## use

### (1) import one or more scalers by their names

- MinMaxScaler
- MaxAbsScaler
- RobustScaler
- StandardScaler
- Normalizer
- DecimalScaler

For example, import DecimalScaler by
```python
from normascaler.scaler import DecimalScaler
```
### (2) Use Decimal scaling method
```python
X_train_scaled, X_train_scaled = DecimalScaler(X_train, X-test)
```
### (3) Display the normalized X_train data in Pandas DataFrame
```python
X_train_scaled
```
### (4) Display the normalized X_test data in Pandas DataFrame
```python
X_test_scaled
```
 ## Documentation
 Examples of a Jupyter note in GitHub: https://github.com/shoukewei/normscaler/blob/main/docs/examples.ipynb