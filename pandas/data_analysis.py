from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing, load_diabetes

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


diabetes_df = pd.read_csv('pandas/diabetes.csv')

type(diabetes_df)

diabetes_df

diabetes_df.shape

print(diabetes_df)

# Exporting a data frame to a csv file 

diabetes_df.to_csv('<file name>')


#Creating a dataframe with random variables

random_df = pd.DataFrame(np.random.rand(20,10))

random_df.head()

random_df.shape


# INSPECTING DATAFRAME 
    # Finding rows and column 

# the last 5 rows of the dataframe 

california_df.tail


# info about the dataframe 

california_df.isnull().sum


# DIABETES DATAFRAME

diabetes_df.head()


print(diabetes_df)



# counting the values based on the labels

 

diabetes_df.head()

diabetes_df.value_counts('Outcome')

print(diabetes_df)


# group the values based on mean

diabetes_df.groupby('Outcome').mean()

print(diabetes_df)

# Statistical measure (Use california dataframe)

    #count or number of values


california_df.count()


print(california_df.count())

# Mean value - cloumn wise

california_df.std()

print(california_df.std())

#minimum value

california_df.min

print(california_df.min)


# max value

california_df.max()

print(california_df.max())

# All statistical measure about the dataframe

california_df.describe()

print(california_df.describe)

# MANIPULATING A DATA FRAME 

# adding a column to a dataframe

diabetes_df['price'] = diabetes_df.Age
print(diabetes_df)

#removing a row 
california_df.drop(index=0,axis=0)
print(california_df.drop(index=0,axis=0))

#drop a column

california_df.drop(columns='MedInc',axis=1)
print(california_df.drop(columns='MedInc',axis=1))

