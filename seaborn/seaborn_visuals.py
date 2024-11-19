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

iris = sns.load_dataset('iris')
iris.head()
print(iris)