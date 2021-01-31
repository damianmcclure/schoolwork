# Used items from the McDonalds menu
menu = {
	"Big Mac": "$3.99",
	"Filet-O-Fish": "$3.79",
	"Chicken McNuggets": "$1.99",
	"McChicken": "$1.29"
}

# Prints all of the items
for item in menu:
	print(item)

choice = input("Choose a menu item: ")
# They choose an item

try:
	if choice in menu:
		# Prints item is price
		print(choice + " is " + menu[choice])
	else: 
		# Occurs if the item is not in the menu dictionary
		print("Item is not on the menu.")
except:
	# An error shouldn't occur, but it's good to have try/except just in case
	print("Input is not on the menu.")
