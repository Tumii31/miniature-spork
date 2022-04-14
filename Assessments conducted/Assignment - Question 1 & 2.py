#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


#Question 1.1
class PatientFileReader():
    def read_file(Patient_Data):
        Patient_Data = open("Patient_Data3.txt", "r")
        poly = Patient_Data.read()
        Patient_Data.close()


# In[2]:


#Question 1.2
filehandler = open("Patient_Data3.txt","r")
print(filehandler)


# In[3]:


#Question 1.3
filehandler.close()


# In[4]:


#Question 1.4
#define text file to open
my_file = open('Patient_Data3.txt', 'r')

#read text file into list 
data = my_file.read()

#display content of text file
print(data)


# In[5]:


#Question 1.5
def getData():
    text = open('Patient_Data3.txt', 'r')
    count = 0
    
    while True:
        count += 1
        line = text.readline()
        
        if not line:
            print('None')
            break
            
        print('Line{}: {}'.format(count, line.strip()))
        
    text.close()


# In[6]:


#Question 1.6
class PatientData():
    def storeIndividual():
        with open('Patient_Data3.txt', 'r') as data:
            list1 = []
            for line in data:
                strip_lines = line.strip()
                list2 = strip_lines.split()
                print(list2)
                m = list1.append(list2)
            print(list1)


# In[7]:


#Question 1.7
def PrintData():
    text = open('Patient_Data3.txt', 'r')
    lines = text.readlines()
    print(lines)
    
    patientno = []
    surname = []
    name = []
    age = []
    sex = []
    weight = []
    
    for l in lines:
        as_list = l.split(",")
        patientno.append(as_list[0])
        surname.append(as_list[1])
        name.append(as_list[2])
        age.append(as_list[3])
        sex.append(as_list[4])
        weight.append(as_list[5])
        
    from tabulate import tabulate
    
    print(" ")
    print("Patient Data")
    print(" ")
    
    d = [ [patientno[0], surname [0], name[0], age[0], sex[0], weight[0]], 
        [patientno[1], surname [1], name[1], age[1], sex[1], weight[1]],
        [patientno[2], surname [2], name[2], age[2], sex[2], weight[2]],
        [patientno[3], surname [3], name[3], age[3], sex[3], weight[3]],
        [patientno[4], surname [4], name[4], age[4], sex[4], weight[4]],
        [patientno[5], surname [5], name[5], age[5], sex[5], weight[5]]]
         
    print(tabulate(d, headers=["PATIENT_NO.", "SURNAME", "NAME", "AGE", "SEX", "WEIGHT(KG)"]))
    


# In[9]:


#Question 1.8
def main():
        #PatientFileReader.Open()
        #PatientFileReader.getAll()
        #PatientFileReader.getData()
        #PatientFileReader.Close()

        PatientData.storeIndividual()
        #PatientData.PrintData()
    
if __name__ == "__main__":
    main()


# # Question 2

# In[ ]:


#Question 2.1
# creating an empty list
lst = []
print("Enter 6 even numbers between 1 - 12")
   
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
print(lst)

# creating an empty list
lst2 = []
print("Enter 4 even numbers between 20 -40")
   
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst2.append(ele) # adding the element
     
print(lst2)


# In[ ]:


#Question 2.2
# Function to merge array in sorted order
def sortedMerge(a, b, res, n, m):
    # Concatenate two arrays
    i, j, k = 0, 0, 0
    while (i < n):
        res[k] = a[i]
        i += 1
        k += 1
    while (j < m):
        res[k] = b[j]
        j += 1
        k += 1
  
    # sorting the res array
    res.sort()
  
    # Driver code
a = lst
b = lst2
n = len(a)
m = len(b)
 
# Final merge list
res = [0 for i in range(n + m)]
sortedMerge(a, b, res, n, m)
print("Sorted merged list :")
for i in range(n + m):
    print( res[i],)


# In[ ]:


#Question 2.3(a)

print(res)


# In[ ]:


import math
 
# Representation of a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
    # Function to insert node
def insert(root, item):
    temp = Node(item)
     
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
     
    return root
 
def display(root):
    while (root != None) :
        print(root.data, end = " ")
        root = root.next
         
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
     
    return root
 
# Driver code
if __name__=='__main__':
    arr = [res]
    n = len(arr)
    root = arrayToList(arr, n)
    print("Linked list in the same order as merged sorted array: ")
    display(root)


# In[ ]:




