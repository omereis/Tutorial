#!/usr/bin/python

import ast
import inspect
print ("Hello, Python!")
t1 = ast.parse("q = a + b / 2")
t2 = ast.parse("q = (a + b) / 2")
f = t1 == t2

print ("Where can I see this string?")
print('Here\'s a string with a single "\'"')
print ("Here's a comment: \n#comment")
name = "Moses"
print ("'name' is '" + name + "'")
len = 4 + 3j
print (abs(len))
dicti = {'1': "one", '2': "two", '3': "three"}

print ('dictionaty of 1 is: ' + dicti['1'])
print("\ndictionary values:")
print(dicti.values())
print("\ndictionary keys:")
print(dicti.keys())
#print("dictionary:\n" + dicti)
#print("Keys:\n" + dicti.keys())
#print("values:\n" + dicti.values())
city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
city_p = {"New York City":'8550405', "Los Angeles":'3971883', "Toronto":'2731571'}
print("Pop. of Toronto:")
print(city_population["Toronto"])
print(city_p["Toronto"])

print("\n")
print (city_population)
print (city_p)