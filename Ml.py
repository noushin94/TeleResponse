import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


#read csv file
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
#print dataframe
print(df)
print(df.columns)
print(df.shape)

#number of columns
num_column = df.shape[1]
print(num_column)

#checking type of each column

for column in df.columns:
    print ({f"{column} has type of {df[column].dtype} and has {df[column].value_counts().sum()} elemnts and has {df[column].isnull().sum()} null value"})

#checking number of objcet columns and int columns
num_obj_column = 0
num_int_column = 0  
for column in df.columns:
   
    if df[column].dtype == "object":
        num_obj_column += 1
    if df[column].dtype == "int64":

        num_int_column += 1


print(f"num_obj_column is {num_obj_column} and num_int_column is {num_int_column}")   


#checking each columns information
def checking_column_information(column):

    print(f"{column} is of the type of {df[column].dtype}  it's distribution is {df[column].value_counts()}")

#loop over all the column except the first column
for column in df.columns[1:]:
    checking_column_information(column)

# evaluate revenue based on phone services and gender
df_revenue = df.groupby(["InternetService"])["MonthlyCharges"].sum().reset_index(name = "total_revenue")
print(df_revenue)


plt.figure(figsize = (8,5))
plt.bar(df_revenue["InternetService"], df_revenue["total_revenue"], color = "skyblue")

#Add labels and titles

plt.xlabel("Internet Service")
plt.ylabel("total revenue")
plt.title("distribution")


#show plot
plt.show()


#check for duplicate
duplicates = df.duplicated()
print(df[duplicates])

#ploting to evaluate distribution
for column in df.select_dtypes(include=["float64", "int64touch "]):
    plt.figure(figsize= (8,5))
    plt.hist(df[column], bins = 30, color = "skyblue")
    plt.xlabel(column)
    plt.ylabel("frequency")
    plt.title(f"distribution of {column}")
    plt.show()

for column in df.select_dtypes(include = ["object", "category"]):
    plt.figure(figsize = (8,5))
    sns.countplot(x= df[column])
    plt.title(f"distribution of {column}")
    plt.xticks(rotation = 45)
    plt.show()


#for column in df.select_dtypes(include = ["float32", "int64"]):


