
# coding: utf-8

# In[ ]:


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

