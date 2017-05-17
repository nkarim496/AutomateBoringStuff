#! python3
UserInventory = {'rope': 1,
             'torch': 6,
             'gold coin': 42,
             'dagger': 1,
             'arrow': 12}
dragonLoot = ['gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'ruby']
def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1

displayInventory(UserInventory)
addToInventory(UserInventory, dragonLoot)
displayInventory(UserInventory)
