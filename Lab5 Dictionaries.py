#Frankie Quintero
# I'm using collections to help with the list and get a solid count of items
from collections import Counter

# will display any inventory passed into it
def displayInventory(inventory):
  print("Inventory:")
  TotalItems = 0
  for item in inventory:
    print(str(inventory[item]) + " " + str(item) )
    TotalItems = TotalItems + inventory[item]
  print('Total number of items: ', TotalItems)
  # reset counter just because
  TotalItems = 0
  

def addToInventory(inventory, addedItems):
    # if passed in two dicts it will put them together
   if(type(addedItems) is  dict):
    for item in addedItems:
      inventory.setdefault(item, 0)
      inventory[item] = inventory[item] + addedItems[item]
      print('Awarded ' + 'item: ' + str(item) + '! New amount: ' + str(addedItems[item]))

    # If passed a list it will read the list, get a count and add them to the inventory
   if(type(addedItems) is  list):
    # Create a temp dict for the recieved items
    tempItems = Counter(addedItems)
    #print(tempItems)
    for item in tempItems:
      inventory.setdefault(item, 0)
      inventory[item] = inventory[item] + tempItems[item]
      print('Awarded ' + 'item: ' + str(item) + '! New amount: ' + str(tempItems[item]))
    


def main(): 

    #Initial inventory
    inventory = {'rope': 1, 'torch': 1, 'gold coins': 148, 'dagger': 1,'Crossbow':1, 'Bolts': 12}
    displayInventory(inventory)
    print('=============================================================================')
    print('Quest Completed')
    print('=============================================================================')
    #Second inventory to test dicts
    QuestReward = {'gold coins': 352, 'Sword': 1,'Saphire': 7,'Emerald': 5}
    addToInventory(inventory, QuestReward)
    #displayInventory(inventory2)
    print('\n')
    print('-----------------------------------------------')
    print('INVENTORY    MAP(1)    QUESTS(3)    MESSAGES(5)    ')
    print('-----------------------------------------------')
    displayInventory(inventory)
    

    #List to be added to inventory
    #inventory3 = ['rope', 'sword', 'sword','secretkey','c(o.O)o','Demon soul', '~mace~' ]
    #addToInventory(inventory, inventory3)
    #print('Congratulations! You\'ve completed the secret quest and you gain a new mystery')
    #displayInventory(inventory)
main()
