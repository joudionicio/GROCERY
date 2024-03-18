#Dictionary
grocery_list = {}
#List
history = []

def add_item():
    '''
    Add Item into List
    '''
    item = input("Please enter an item to add to your grocery list: ")
    quantity = input(f"Please enter the quantity of {item} you need to purchase: ")
    cost =input(f"Price enter the price of {item}: ")
    grocery_list= {'item':item, 'quantity':int(quantity),'cost':float(cost)}
    history.append(grocery_list)


def edit_item():
    '''
    Edit Item into List
    '''
    #edit an item from the list
    print("\n Select a item on the list to Edit.....\n")
    index = 1
    for item in history:
        print("[" + str(index) + "]" + item['item'])
        index +=1
    
    list_to_edit = {}
    item_to_edit = input("Which item do you want to edit? ")
    quantity_to_edit = input(f"Please enter the quantity of {item_to_edit} you need to edit: ")
    cost_to_edit = input(f"Price enter the price of {item_to_edit} to edit: ")
    for item in history:
        if item['item'] == item_to_edit:
            list_to_edit = {'item':item_to_edit, 'quantity':int(quantity_to_edit),'cost':float(cost_to_edit)}
            #Get Index of dictionary
            history[history.index(item)] = list_to_edit
            #print(history.index(item))
            break
            
    displays_items()
            
def remove_item():
    #Global variables can be used by everyone, both inside of functions and outside.
    global history
    #show list items
    print("\n Select a item on the list to remove.....\n")
    for item in history:
        print("[" + item['item'] + "]")
    #take out an item 
    #grocery_list #since we set grocery list to a new list
    items_to_remove = input("Which item do you want to remove? ")
    newlist = history.copy() # we create a new list
    for item in history:
        if item['item'] == items_to_remove:
            newlist.remove(item)
    history = newlist

def displays_items():
    #print out the list
    print("\n Here is the grocery list.....\n")
    for item in history:
        print(f"{item['item']}: {item['quantity']} (${item['cost']} per unit)")

def calculate_items():
    #result of the list
    grand_total = 0
    for item in history:
        item_total = item['quantity']*item['cost']
        grand_total += item_total
    
    print("TOTAL COST: $",  grand_total)

def menu_grocery():
    print("\n\t***  Menu:  ***\n")
    print("1. Add an item to the grocery list")
    print("2. Edit an item on the grocery list")
    print("3. Remove an item from the grocery list")
    print("4. Display the grocery list")
    print("5. Calculate the total cost of the grocery list")
    print("6. Quit")
    user_option = int(input("Please enter your choice 1-6: "))
    return user_option

#Main program
print("\t**********************************************")
print("\t***  Welcome to the Grocery List Manager!  ***")
print("\t**********************************************")  



while True:
        item = input("Please enter an item to add to your grocery list: ")
        quantity = input(f"Please enter the quantity of {item} you need to purchase: ")
        #float mean that the user can put prices with cents(decimals)
        cost = float(input(f"Please enter the price of {item}: "))
        #this is when the list start to develop
        grocery_list = {'item':item, 'quantity':int(quantity),'cost':float(cost)}
        history.append(grocery_list)
        
        add_more = input("Would you like to add another item? (y/n): ")
        if add_more == "y":
            continue
        elif add_more == "n":
            break

print("\n\t***Your Grocery List:  ***")
for item in history:
    #the code ":.f" mean that the decimals only limited to 2 decimals before the point 
    print(f"{item['item']}: {item['quantity']} ({item['cost']} per unit)")


while True:
        #User option
        user_option = menu_grocery()
        if user_option == 1:
            #add item
            add_item()
        elif user_option == 2:
            #edit item
            edit_item()
        elif user_option == 3:
            #remove item
            remove_item()
        elif user_option == 4:
            #displays items
            displays_items()
        elif user_option == 5:
            #calculate
            calculate_items()
        else:
            #quit
            break