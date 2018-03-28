import pandas as pd

list1 = [{'name':'yyy', 'score':78}, {'name':'www', 'score':78}, {'name':'yyy', 'score':22}]
list2 = [{'name':'yyy', 'score':79}, {'name':'www', 'score':79}, {'name':'yyy', 'score':23}]
df = pd.DataFrame(list1,list2)
result = df.groupby(['name'])

#print result
#jsonData = dict(jsonData.items()+jsonData.items())
print df
