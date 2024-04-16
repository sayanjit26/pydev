import pandas as pd


dat={
    'name':['sayan','raj','mili'],
    'grade':['a','b','c'],
    'marks':[67,89,56],
    'event':['rain','sunny','fog']
}

df=pd.DataFrame(dat)
print(df['event','grade'])

