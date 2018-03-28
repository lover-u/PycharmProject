#!/usr/bin/python
def adddict(dict1,dict2):
  xin = {}
  for key in dict1.keys():
    xin[key] = dict1[key]
  for key in dict2.keys():
    xin[key] = dict2[key]
  return xin
s1 = {1:222,'c':'d','e':'f'}
s2 = {2:333,'g':'h','i':'j'}
print adddict(s1,s2)