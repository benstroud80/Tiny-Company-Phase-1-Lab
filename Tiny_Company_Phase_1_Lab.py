class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


# Prompt user for two items and create two objects of the ItemToPurchase class
item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))

item2 = ItemToPurchase()
print("\nItem 2")
item2.item_name = input("Enter the item name:\n")
item2.item_price = float(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))

# Print the cost of each item
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

# Calculate and print the total cost
total_cost = item1.item_quantity * item1.item_price + item2.item_quantity * item2.item_price
print("\nTotal:", "${:.2f}".format(total_cost))

