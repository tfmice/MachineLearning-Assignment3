import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("listings.csv", delimiter=",")
dataset["reviews_per_month"] = dataset["reviews_per_month"].replace(",", ".", regex=True)
dataset = dataset.dropna()
dataset = dataset.astype({"price" : "int32", "minimum_nights" : "int32", "number_of_reviews" : "int32", "calculated_host_listings_count" : "int32", "availability_365" : "int32", "reviews_per_month" : "float64"})
dataset["last_review"] = pd.to_datetime(dataset["last_review"], format= "%Y-%m-%d")
print(dataset["room_type"].unique())
dataset["room_type"] = pd.Categorical(dataset["room_type"], dataset["room_type"].unique())
dataset["room_type"] = dataset["room_type"].cat.rename_categories([1,2,3])
# print(dataset.dtypes)
# print(dataset.isna().values.any())
# print(dataset.head())
# print(dataset[["room_type"]])
# print(len(dataset))
type1 = 0
type2 = 0
type3 = 0
# print(dataset.iloc[1]["price"])
for i in range(len(dataset)):
    if dataset.iloc[i]["room_type"] == 1:
        type1 = type1+1
    if dataset.iloc[i]["room_type"] == 2:
        type2 = type2+1
    if dataset.iloc[i]["room_type"] == 3:
        type3 = type3+1
    # print(i)
# print(type1, type2, type3)
probability1 = type1/len(dataset)
probability2 = type2/len(dataset)
probability3 = type3/len(dataset)

mean = 1 * probability1 + 2 * probability2 + 3 * probability3
print("Mean of room_type : " + str(mean))
print("Variance of reviews_per_month : " + str(dataset["reviews_per_month"].var()))