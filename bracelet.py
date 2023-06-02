# This is a dictionary holding the bracelets inventory.
bracelets_inventory = {
    1: {"title": "Gold Bracelet", "price": "$300", "details": "24 carat gold bracelet"},
    2: {"title": "Silver Bracelet", "price": "$100", "details": "99.99% pure silver bracelet"},
    3: {"title": "Diamond Bracelet", "price": "$1000", "details": "Beautiful diamond bracelet"},
    4: {"title": "Pearl Bracelet", "price": "$500", "details": "Elegant pearl bracelet"},
    5: {"title": "Ruby Bracelet", "price": "$800", "details": "Beautiful ruby bracelet"},
}

def display_inventory(inventory):
    for item_num, item_info in inventory.items():
        print(f"Item Number: {item_num} , Title: {item_info['title']}")

# Greeting the user
print("Welcome to our Jewelry Shop!")

# Calling the function to display the inventory
display_inventory(bracelets_inventory)

# This list will hold the item numbers of the bracelets that the user has viewed
viewed_items = []

# Variable to keep the program running until user decides to quit
keep_running = True

while keep_running:
    user_input = input("\nPlease enter the item number to see the price and details or 'q' to quit: ")

    if user_input.lower() == 'q':
        keep_running = False
    else:
        item_number = int(user_input)
        if item_number in bracelets_inventory:
            # If the item number is valid, add it to the viewed_items list
            viewed_items.append(item_number)
            item_info = bracelets_inventory[item_number]
            print(f"\nTitle: {item_info['title']}")
            print(f"Price: {item_info['price']}")
            print(f"Details: {item_info['details']}")
        else:
            print("\nInvalid item number. Please try again.")

print("\nThank you for visiting our Jewelry Shop! Have a nice day!")

# At the end of the program, print the item numbers of the bracelets that the user has viewed
print("\nYou have viewed the following items:")
for item_number in viewed_items:
    print(f"Item Number: {item_number} , Title: {bracelets_inventory[item_number]['title']}")
