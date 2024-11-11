from sklearn.datasets import fetch_california_housing
import pandas as pd

# Fetch the California housing dataset
california_housing = fetch_california_housing()

# Convert the dataset into a pandas DataFrame
california_df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)

# Add the target (house values)
california_df['target'] = california_housing.target

# Show the first few rows of the dataset
print(california_df)
 

california_df.head()
california_df.shape

# Importing the data of a csv file to a pandas data frame 
from sklearn.datasets import load_diabetes

diabetes_df = pd.read_csv('diabetes.csv')

type(diabetes_df)

diabetes_df

diabetes_df.shape

print(diabetes_df)