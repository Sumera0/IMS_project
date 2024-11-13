# Dictionary to store inventory items
inventory = {}
purchased_items = []

def add_item():
    part_number = int(input("Enter part number: "))
    if part_number in inventory:
        print(f"That part number already exists :(, changing value to {part_number + 1}")
        part_number += 1
    part_price = float(input("Enter part price: "))
    part_description = input("Enter part description: ")
    part_stock = int(input("Enter part stock: "))
    inventory[part_number] = {
        "description": part_description,
        "price": part_price,
        "stock": part_stock
    }
    print(f"Part number: {part_number} Description: {part_description} Price: {part_price:.2f} Stock: {part_stock}")
    print("Part was added successfully!")

def remove_item():
    part_number = int(input("Enter part number to remove: "))
    if part_number in inventory:
        del inventory[part_number]
        print(f"Part number {part_number} was removed successfully!")
    else:
        print("Part not found!")

def edit_item():
    part_number = int(input("Enter part number to edit: "))
    if part_number in inventory:
        print(f"Current details: {inventory[part_number]}")
        part_price = float(input("Enter new part price: "))
        part_description = input("Enter new part description: ")
        part_stock = int(input("Enter new part stock: "))
        inventory[part_number] = {
            "description": part_description,
            "price": part_price,
            "stock": part_stock
        }
        print(f"Part number {part_number} updated successfully!")
    else:
        print("Part not found!")

def list_items():
    if not inventory:
        print("No items in the inventory.")
    else:
        for part_number, details in inventory.items():
            print(f"Part number: {part_number} | Description: {details['description']} | Price: {details['price']:.2f} | Stock: {details['stock']}")

def inquire_part():
    part_number = int(input("Enter part number to inquire: "))
    if part_number in inventory:
        details = inventory[part_number]
        print(f"Part number: {part_number} | Description: {details['description']} | Price: {details['price']:.2f} | Stock: {details['stock']}")
    else:
        print("Part not found!")

def purchase():
    part_number = int(input("Enter part number to purchase: "))
    if part_number in inventory:
        quantity = int(input("Enter quantity to purchase: "))
        if quantity <= inventory[part_number]['stock']:
            inventory[part_number]['stock'] -= quantity
            purchased_items.append({
                "part_number": part_number,
                "description": inventory[part_number]['description'],
                "price": inventory[part_number]['price'],
                "quantity": quantity
            })
            print(f"Purchased {quantity} of part number {part_number} successfully!")
        else:
            print("Not enough stock available!")
    else:
        print("Part not found!")

def checkout():
    if not purchased_items:
        print("No items have been purchased.")
    else:
        total = sum(item['price'] * item['quantity'] for item in purchased_items)
        print("Purchased items:")
        for item in purchased_items:
            print(f"Part number: {item['part_number']} | Description: {item['description']} | Price: {item['price']:.2f} | Quantity: {item['quantity']}")
        print(f"Total: {total:.2f}")
        purchased_items.clear()

def show_purchased_items():
    if not purchased_items:
        print("No items have been purchased.")
    else:
        print("Purchased items:")
        for item in purchased_items:
            print(f"Part number: {item['part_number']} | Description: {item['description']} | Price: {item['price']:.2f} | Quantity: {item['quantity']}")

def display_menu():
    print("""
Welcome to IMS
A-Add an item
R-Remove an item
E-Edit specifics of an item
L-List all items
I-Inquire about a part
P-Purchase
C-Checkout
S-Show all parts purchased
Q-Quit
remove-Remove an item from the cart
help-See all commands again
""")

def main():
    display_menu()
    while True:
        choice = input("What would you like to do? ").lower()
        if choice == 'a':
            add_item()
        elif choice == 'r':
            remove_item()
        elif choice == 'e':
            edit_item()
        elif choice == 'l':
            list_items()
        elif choice == 'i':
            inquire_part()
        elif choice == 'p':
            purchase()
        elif choice == 'c':
            checkout()
        elif choice == 's':
            show_purchased_items()
        elif choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'help':
            display_menu()
        else:
            print("Invalid choice. Type 'help' to see all commands.")

if __name__ == "__main__":
    main()
