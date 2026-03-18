import pandas as pd
df = pd.Series([23, 24, 78, 45])
print(df.max())
print(df.min())
print(df.sum())
print(df.count())
import pandas as pd
ResultSheet={
'Arnab': pd.Series([90, 91, 97],index = ['Maths', 'Science', 'Hindi']),
'Ramit': pd.Series ([92, 81, 96], index=['Maths', 'Science', 'Hindi']),
'Samridhi' : pd.Series ([89, 91, 88], index=['Maths', 'Science', 'Hindi']),
'Riya' : pd.Series ([81, 71, 67], index=['Maths', 'Science', 'Hindi']),
'Mallika' : pd. Series ([94, 95, 99], index = ['Maths', 'Science', 'Hindi'])
}
ResultDF =pd.DataFrame(ResultSheet)
print (ResultDF)
print(ResultDF['Riya'])
print (ResultDF.loc[['Maths', 'Hindi']])
print (ResultDF.loc['Maths']>90)
print(ResultDF.loc['Science'].sum())
print(ResultDF.max(axis=1))
print(ResultDF.max())
print(ResultDF.count())
