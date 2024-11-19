# importing the libraries 

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# NOTE ;seaborn has some built in datasets ; Total bill vs Tip data set

tips  = sns.load_dataset('tips')
tips.head()
print(tips)


# setting a theme for the plots
sns.set_theme()

#visualise the data 
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tip= sns.load_dataset("tips")

# Plot
sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",  # Correct column name
    style="smoker",
    col="time",
    hue="smoker",
    size="size"
)
plt.show()

#load the iris dataset

iris = sns.load_dataset("iris")
iris.head()
print(iris.head())

# Scatter plot 
    #visualize the iris dataset
sns.relplot(x='sepal_length',y='petal_length',hue='species',data=iris)
plt.show()

# load the titanic dataset

titanic = sns.load_dataset("titanic")
titanic.head()
print(titanic.head())

# count plot

sns.countplot(x='class',data=titanic)

#to know how many people survived

sns.countplot(x='survived', data=titanic)
plt.show()


# Bar Chart
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()

# House Price dataset

        #Import this dataset

from sklearn.datasets import fetch_california_housing

house_boston=fetch_california_housing
house=pd.DataFrame (house_boston.data,columns=house_boston.featurenames)


