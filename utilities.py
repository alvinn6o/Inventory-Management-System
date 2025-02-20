# handles user interaction and validates user input to manipulate item data
from items import Item

def menu():
    while True:
        try:
            print("\n1. View inventory")
            print("2. Search item")
            print("3. Update item quantity/price")
            print("4. Add new item")
            print("5. Remove existing item")
            print("6. Input bulk shipment")
            print("7. View net value")
            print("8. View item history")
            print("0. Exit\n")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                Item.view_inventory()
            elif choice == "2":
                search_item()
            elif choice == "3":
                update_item()
            elif choice == "4":
                add_item()
            elif choice == "5":
                remove_item()
            elif choice == "6":
                #bulk_shipment()
                print("Not implemented yet")
                continue
            elif choice == "7":
                Item.calculate_net_total()
            elif choice == "8":
                #view_item_history()
                print("Not implemented yet")
                continue
            elif choice == "0":
                print("Exiting")
                exit()
            else:
                print("Invalid choice: Please enter a number between 1-9")
        except Exception as e:
            print(f"Error: {e}")

                

def add_item():
    while True:
        name = input("Enter name of item to add: ").strip()
        if not name:
            print("Error: please enter a name")
            continue
        if Item.find_item(name):
            print(f"Error: item {name} already exists")
            return
        break

    while True:
        quantity = input(f"(Optional) Enter quantity of {name}: ")
        if not quantity:
            quantity = 0
        elif not quantity.isdigit():
            print("Error: enter valid quantity")
            continue
        else:
            quantity = int(quantity)
            if quantity < 0:
                print("Error: quantity cannot be negative")
                continue
        break

    while True:
        price = input(f"(Optional) Enter price of {name}: ")
        if not price:
            price = 0
        elif not price.isdigit():
            print("Error: enter valid price")
            continue
        else:
            price = float(price)
            if price < 0:
                print("Error: price cannot be negative")
                continue
        break

    try:
        Item.add_item(name, quantity, price)
    except Exception as e:
        print(f"Error: {e}")

def remove_item():
    name = input("Enter name of item to remove: ").strip()
    if not name:
        print("Error: Please enter a name")
        return
    Item.remove_item(name)


def update_item():
    name = input("Enter an item name to update: ").strip()
    if not name:
        print("Error: Please enter a name")
        return

    current_item = Item.find_item(name)
    if not current_item:
        print(f"Item '{name}' not found.")
        return

    while True:
        quantity = input(f"Current quantity: {current_item.quantity}. Enter new quantity (or press Enter to keep current): ").strip()
        if not quantity:
            quantity = None
            break
        try:
            quantity = int(quantity)
            if quantity < 0:
                print("Error: quantity cannot be negative")
                continue
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    while True:
        price = input(f"Current price: ${current_item.price:.2f}. Enter new price (or press Enter to keep current): $").strip()
        if not price:
            price = None
            break
        try:
            price = float(price)
            if price < 0:
                print("Error: price cannot be negative")
                continue
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    try:
        Item.update_item(name, quantity, price)
    except Exception as e:
        print(f"Error: {e}")


def search_item():
    name = input("Search for item: ").strip()
    if not name:
        print("Error: Please enter a name")
        return
    
    found = Item.find_item(name)
    if found:
        print(f"Item found: {found.name}")
        print(f"Quantity: {found.quantity}")
        print(f"Price: ${found.price:.2f}")
        print(f"Total value: ${found.total:.2f}")
    else:
        print(f"Item '{name}' not found.")


