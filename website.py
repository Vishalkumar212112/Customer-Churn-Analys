import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# read data from csv file into a dataframe
df = pd.read_csv("Customer Churn.csv", encoding="latin1")
# df.head()

df.info()
# print(df)


# replace blamnks wih  0 as and 
df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")
print(df.info())


df.isnull() . sum() . sum()
# print(df)

df.describe()
# print(df)

df["customerID"].duplicated() . sum()
print(df)


# vonverted 0 and 1 values of senior citizen to yes/no to make it easier to under
def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"
    
df["SeniorCitizen"] = df["SeniorCitizen"] . apply(conv)
print(df.head(10))





# form the given pie chart
ax = sns.countplot(x = df["Churn"] , data = df)

ax.bar_label(ax.containers[0])
plt.title("Count of customer by Churn")


plt.figure(figsize=(3,4))
gb = df.groupby("Churn") .agg({"Churn":"count"})
plt.pie(gb["Churn"], labels= gb.index, autopct= "%1.2f%%" )
plt.title("Percentage of Churn Customer", fontsize =10)
# plt.show()

plt.figure(figsize=(3,3))
sns.countplot(x = "gender", data=df , hue ="Churn")
plt.title("Churn by  Gender")
plt.show()