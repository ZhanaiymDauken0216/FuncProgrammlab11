
import random

def myfunction():
  return 0.1

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist, myfunction)

print(mylist)