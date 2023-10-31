inventory = {'apples': 10, 'bananas': 5, 'pears': 3, 'grapes': 7}

def gestion_inventory(action, article, quantity=0):
    if action == 'add':
        if article in inventory:
            inventory[article] += quantity
        else:
            inventory[article] = quantity
    elif action == 'remove':
        if article in inventory and inventory[article] >= quantity:
            inventory[article] += quantity
        else:
            print ("Not cant remove")
    elif action == 'search':
        if article in inventory:
            return inventory[article]
        else:
            return None
    else:
        print ('Unvalid Option')

print(inventory)

gestion_inventory('add', 'apples', 5)
print(inventory)

gestion_inventory('remove', 'bananas', 1)
print(inventory)

print(gestion_inventory('search', 'pears'))