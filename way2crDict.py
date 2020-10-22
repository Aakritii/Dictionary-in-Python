
# coding: utf-8
# Creating an empty dictionary 
myDict = {} 

#adding list as value 
myDict["key1"] = [1, 2] 
myDict["key2"] = ["Geeks", "For", "Geeks"] 

print(myDict) 

#creating an empty dictionary using dict function
myDict1=dict()

# Adding list as value 
myDict1["key1"] = [1, 2] 
  
# creating a list 
lst = ['Geeks', 'For', 'Geeks'] 

# Adding this list as sublist in myDict 
myDict1["key1"].append(lst) 

print(myDict1)

myDict2={}

# Iterating the elements in list 
for val in lst: 
    for ele in range(int(val), int(val) + 2):  
        myDict2.setdefault(ele, []).append(val) 
print(myDict2)


#----------------Collaborated by Muskan Salampuria-----------#
        
# Creating a dictionary of lists using list comprehension 
myDict3 = dict((val, range(int(val), int(val) + 2)) 
                  for val in ['1', '2', '3']) 
  
print(myDict3) 
     
  
# Importing defaultdict 
from collections import defaultdict 
  
dict1 = [('Happy', 1), ('Birthday', 2), ('Muskan', 3)] 
myDict4 = defaultdict(list) 
  
# iterating over list of tuples 
for key, val in dict1: 
    myDict4[key].append(val) 
  
print(myDict4) 


#importing json 
import json 
  
#Initialisation of list 
dict2 = [('Happy', 1), ('Birthday', 2), ('Muskan', 3)] 
  
#Initialisation of dictionary 
myDict5 = {} 
  
#using json.dump() 
hash = json.dumps(dict2) 
  
#creating a hash 
myDict5[hash] = "converted"
  
#Printing dictionary 
print(myDict5) 
=======
# Importing defaultdict 
from collections import defaultdict 
  
lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)] 
orDict = defaultdict(list) 
  
# iterating over list of tuples 
for key, val in lst: 
    orDict[key].append(val) 
  
print(orDict)
