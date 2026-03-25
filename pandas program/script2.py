import pandas as pd
data=pd.read_csv("restaurant_orders.csv")
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',10)
print(data)
data.to_excel("restaurant_orders.xlsx",index=False)
