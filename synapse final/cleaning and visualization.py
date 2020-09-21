import json
import pandas as pd
from matplotlib import pyplot as plt

with open('data.json') as f:
    d = json.load(f)

# converting nested json file in dataframe
df = pd.json_normalize(d['data'])

# renaming columns to required format
df.rename(columns={"location.latitude":"latitude","location.city":"city","location.state":"state","location.longitude":"longitude",'location.zip_code':"zipcode"},inplace=True)

# applying provided condtions given in question
# like Event type should be Fund Project,
# category can be sports or environment
# minimum donation amount should be 20
condition_satisfiers =( (df["event_name"] == "Fund Project") & ( (df["category"] == "Sports")  | (df["category"] =="Environment") ) & (df["amount"] >= 20) )

# making a dataframe of required condition
df = df[condition_satisfiers]
print(df.isna().sum())
# After Checking, this dataframe has no nan values
# now as we have made a dataframe of required conditon, lets move to Visualization


# VISUALIZATION

plt.style.use("fivethirtyeight")

plt.figure(0)

sports_category = df["category"] == "Sports"
environment_category = df["category"] == "Environment"

category_count=[sports_category.sum(),environment_category.sum()]
category=["Sports","Environment"]
colors=["cyan","yellow"]

plt.pie(category_count,labels=category,colors=colors,shadow=True,startangle=90,wedgeprops={"edgecolor":"black",},autopct="%1.1f%%")

plt.title("Category Distribution")
plt.tight_layout()


plt.figure(1)

male = df["gender"] == "M"
female = df["gender"] == "F"
others = df["gender"] == "U"

gender_count=[male.sum(),female.sum(),others.sum()]
gender=["Male","Female","Others"]
colors=["lightgreen","blueviolet","crimson"]

plt.pie(gender_count,labels=gender,colors=colors,shadow=True,startangle=180,wedgeprops={"edgecolor":"black",},autopct="%1.1f%%")

plt.title("Gender Distribution")
plt.tight_layout()


plt.figure(2)

amount_list = df["amount"].to_list()
amount_list = [int(i) for i in amount_list]

parts=[10,20,30,40,50,60,70,80,90,100]
plt.hist(amount_list,bins=parts,edgecolor="black",color="orange")

plt.title("Fund Classifier")
plt.xlabel("Amount funded")
plt.ylabel("No of People")
plt.tight_layout()

plt.figure(3)

active_cities_dataframe = df["city"].value_counts().head(7)
active_cities_list = active_cities_dataframe.index.values
active_cities_count =  active_cities_dataframe.to_list()

plt.pie(active_cities_count,labels=active_cities_list,colors=["violet","indigo","blue","green","yellow","orange","red"],shadow=True,startangle=180,wedgeprops={"edgecolor":"black",},autopct="%1.1f%%")

plt.title("Top 7 funding cities")
plt.tight_layout()

plt.figure(4)

active_states_dataframe = df["state"].value_counts().head(7)
active_states_list = active_states_dataframe.index.values
active_states_count =  active_states_dataframe.to_list()

plt.pie(active_states_count,labels=active_states_list,colors=["bisque","deepskyblue","hotpink","greenyellow","silver","lavender","snow"],shadow=True,startangle=180,wedgeprops={"edgecolor":"black",},autopct="%1.1f%%")

plt.title("Top 7 funding states")
plt.tight_layout()

plt.figure(5)

age_dataframe= df["age"].value_counts()
print(age_dataframe)
age_group = age_dataframe.index.values
print(age_group)
age_group_count = age_dataframe.to_list()
print(age_group_count)

plt.scatter(age_group,age_group_count,s=50,c="black",edgecolors="white",linewidths=2,alpha=0.75)
plt.title("Activity according to Age")
plt.xlabel("Age Group")
plt.ylabel("Participation")

plt.show()