#BECS Project 1: To Do List
#Luke Berry (CS++)

import shelve

#Initializes variable used to store user response
response = ""

#Temp list temporarily stores the key values of the to do list for use in removing an item
tempList = []

#shelve initialization
s = shelve.open('persistentList.db')

#Displays list of elements in to do list variable
def displayList():
    print("To-Do List: ")
    current = 1
    for key in s:
        print(f"{current}. {key}")
        current += 1

#Used to add new items to the to do list, and displays the list afterwards
def add():
    newItem = input("Which task would you like to add?: ")
    s[newItem] = len(s)
    print(f"{newItem} has been added to your to-do list.")
    displayList()

#Allows user to remove item from shelve list, and displays new list after
def remove():
    removingItem = input("Which task would you like to remove?")
    for k in s:
        tempList.append(k)
    try: 
        s.pop(tempList[int(removingItem) - 1])
        tempList.clear()
    except Exception:
        print("That item does not exist.")
    displayList()

#Runs user response through system to find out what the user would like to do with the list
def firstMenu():
    if response == 'q' or response == 'quit':
        print("Thanks for using our program")
        exit() #exits program if user decides to quit
    elif response == 'a' or response == 'add':
        add()
        onStart() #Re-runs opening flow once an action is completed
    elif response == 'r' or response == 'remove':
        displayList()
        remove()
        onStart()
    elif response == 's' or response == 'show':
        displayList()
        onStart()
    elif response == 'c' or response == 'clear':
        print("Clearing your to-do list.")
        s.clear()
        onStart()
    else:
        print("Error, invalid input. Please input the first letter or full name of menu you'd like to open.")
        onStart()

#Runs when any action is completed
def onStart():
    print("\n")
    global response
    response = input("[Q]uit / [A]dd / [R]emove / [S]how / [C]lear \n")
    response = response.lower()
    firstMenu()

print("Welcome to the To-Do List application!")
onStart()