import os
import time

print ("welcome to your to-do list manager.")
print()
toDoList = []

def printList():
  os.system('clear')
  counter = 1 
  print()
  for item in toDoList:
    print(f"{counter}. {item}")
    counter += 1
  print()

while True:
  print()
  menu = input ("Do you want to view, add, edit, delete or remove an item from the to do list?")
  if menu == "add":
    print()
    item = input ("what do you want to add?")
    if item in toDoList:
      print ("this item is already in the list")
      print()
    else:
      toDoList.append(item)
  elif menu == "remove":
    item = input ("what do you want to remove?")
    if item in toDoList:
      doubleCheck = input ("are you sure you want to remove this?")
      if doubleCheck == "yes":
        toDoList.remove(item)
      else:
        print ("okay, we won't remove it.")
    else:
      print(f"{item} was not in the list")
  elif menu == "view":
    printList()
  if menu == "edit":
    printList()
    item = input ("what do you want to edit?")
    new = input ("what do you want to change it to?")
    if item in toDoList:
      toDoList.remove(item)
      toDoList.append(new)
    else:
      print ("item is not in the list")
  elif menu == "delete":
    toDoList= []
    time.sleep(1)
    os.system('clear')