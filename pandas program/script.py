import by
import pandas as pd
data=pd.read_csv("restaurant_orders.csv")

#PROBLEM 1
print("PROBLEM 1:",data.head(10))
#PROBLEM 2
print("PROBLEM 2: ",data["Food Item"],["price"])
#PROBLEM 3
print("PROBLEM 3: ",data["Quantity"]>3)
#PROBLEM 4
print("PROBLEM 4: ",data["Payment Method"]=="Cash")
#PROBLEM 5
print("PROBLEM 5: ",data.sort_values("Quantity"))
#PROBLEM 6
print("PROBLEM 6: ",len(data))
#PROBLEM 7
print("PROBLEM 7: ",data.sort_values("Price",ascending=False).head(2))
#PROBLEM 8
data["Total"]=data["Quantity"]*data["Price"]
print("PROBLEM 8: ",data["Total"])
#PROBLEM 9
print("PROBLEM 9: ",data["Price"].mean())
#PROBLEM 10
print("PROBLEM 10: ",data["Category"].value_counts())