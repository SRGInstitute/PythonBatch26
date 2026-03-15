import pandas as pd
resultsheet={'rachit':pd.Series([90,91,97], index=['Math','Science','Hindi']),
'Sudhish':pd.Series([89,92,88],index=['Math','Science','Hindi']),
'Ankit':pd.Series([87,76,78],index=['Math','Science','Hindi'])}

ResultDF=pd.DataFrame(resultsheet)
print(ResultDF)
print(ResultDF.loc['Science'])
