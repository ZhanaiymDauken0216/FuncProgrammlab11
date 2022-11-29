#Создание списка случайных чисел в Python с помощью функции random() 
# Python3 program to demonstrate
# the use of random() function .
 
import random 
from random import random
  
lst = []
 
for i in range(10):
  lst.append(random())
   
# Prints random items
print(lst)