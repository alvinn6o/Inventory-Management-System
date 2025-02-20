# Item class that handles reading/writing to json file
# updates item data with the input from utility functions

import csv
import json
from datetime import datetime

class Item:
    def __init__(self, name, quantity: int = 0, price: float = 0.0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price

    # pass TO json file (4 params)
    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "totalValue": self.total
        }

    # get FROM json file (3 params, aligning with class params)
    def from_dict(data):
        return Item(data["name"], data["quantity"], data["price"])
    

    @staticmethod
    def view_inventory():
        try:
            items_list = Item.load_items()
            
            if not items_list:  # If list is empty
                print("\nInventory is empty!")
                return
            
            print("\nCurrent Inventory:")
            print("-" * 30)
            for item in items_list:
                print(f"{'Name:':<15}{item.name}")
                print(f"{'Quantity:':<15}{item.quantity}")
                print(f"{'Price:':<15}${item.price:.2f}")
                print(f"{'Total Value:':<15}${item.total:.2f}")
                print("-" * 30)
                
        except Exception as e:
            print(f"Error reading inventory: {e}")
    

    @staticmethod
    def load_items():
        try:
            with open("items.json", "r") as json_file:
                items_data = json.load(json_file)
                return [Item(item["name"], item["quantity"], item["price"]) for item in items_data]
        except FileNotFoundError:
            return []
    

    # save items to json file
    @staticmethod
    def save_items(items_list):
        try:
            with open("items.json", "w") as json_file:
                json_data = [item.to_dict() for item in items_list]
                json.dump(json_data, json_file, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def find_item(name):
        """Helper method to find an item by name"""
        items_list = Item.load_items()
        return next((item for item in items_list if item.name.lower() == name.lower()), None)

    @staticmethod
    def remove_item(name):
        try:
            items_list = Item.load_items()
            new_items_list = [item for item in items_list if item.name.lower() != name.lower()]
            
            if len(new_items_list) == len(items_list):
                print(f"Item '{name}' not found.")
                return
                
            Item.save_items(new_items_list)
            print(f"Item '{name}' has been removed.")
            
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def update_item(name, quantity=None, price=None):
        try:
            items_list = Item.load_items()
            
            for i, item in enumerate(items_list):
                if item.name.lower() == name.lower():
                    if quantity is not None:
                        items_list[i].quantity = quantity
                    if price is not None:
                        items_list[i].price = price
                    items_list[i].total = items_list[i].quantity * items_list[i].price
                    

                    Item.save_items(items_list)
                    print(f"Item '{name}' has been updated successfully! With quantity: {quantity} and price: ${price:.2f}")
                    return
            print(f"Error: item '{name}' not found")
            return
        except Exception as e:
            print(f"Error: {e}")
            

    @staticmethod
    def add_item(name: str, quantity: int, price: float):
        """Add a new item to inventory"""
        try:
            items_list = Item.load_items()
            items_list.append(Item(name, quantity, price))
            Item.save_items(items_list)
            print(f"Item '{name}' added successfully!")
        except Exception as e:
            print(f"Error: {e}")
            

    @staticmethod
    def calculate_net_total():
        items_list = Item.load_items()
        net_value = sum(item.total for item in items_list)
        try:
            with open("netVal.CSV", "a") as csv_file:
                writer = csv.writer(csv_file)
                if csv_file.tell() == 0:
                    writer.writerow(["date_time","net_value"])
                writer.writerow([datetime.now(),f"{net_value:.2f}"])
            print(f"Net value: ${net_value:.2f} logged")
        except Exception as e:
            print(f"Error: {e}")




