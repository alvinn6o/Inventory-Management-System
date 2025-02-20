# Inventory-Management-System
A Python-based inventory management system that allows users to track, modify, and monitor their inventory items. The system provides a command-line interface for managing products, including their quantities and pricing, while maintaining a historical log of total inventory value.


# Inventory Management System
A Python-based command-line inventory management system for tracking and managing product inventory.

## File Structure

### Python Files
- **`main.py`**: Entry point of the program, handles menu loop and program execution.
- **`items.py`**: Contains the `Item` class and all core data operations.
- **`utilities.py`**: Contains user interface functions and input handling.

### Data Files
- **`items.json`**: Stores the inventory data in JSON format. Each item contains a name, quantity, price, and automatically calculated total value. The file is automatically created on the first item addition and is updated whenever items are added, modified, or removed.
- **`netVal.csv`**: Logs historical net value of inventory with timestamps. The file is created when first viewing net value, and a new entry is added each time net value is calculated. Format includes `DateTime` and `NetValue` columns.

## Setup and Usage

### Requirements
- Ensure Python 3.x is installed.
- Run the program using:
  ```bash
  python main.py


## To-Do / Planned Features
- [ ] Implement bulk shipment processing
- [ ] Implement item history
- [ ] Implement sorting function by alphabetical order, price, quantity, net total
- [ ] Improve error handling for invalid inputs  
- [ ] Add a graphical user interface (GUI)  


 ## Menu Options
- **View inventory**  
- **Search item**  
- **Update item price/quantity**  
- **Add new item**  
- **Remove existing item**  
- **Input bulk shipment** 
- **View net value**
- **View item transaction history**
- **Exit**  


## Data Management


### `items.json`
- Maintains the current state of all inventory items.  
- Automatically created when the first item is added.  
- Updated with every inventory modification.  
- Each item contains:  
  - `name`  
  - `quantity`  
  - `price`  
  - `total value`  

### `netVal.csv`
- Tracks historical total inventory value.  
- Created automatically when net value is first calculated.  
- New entries are appended with each calculation.  
- Each entry includes:  
  - `timestamp`  
  - `total value of all inventory`  

## Error Handling
- Comprehensive input validation prevents negative quantities and prices.  
- Handles file I/O exceptions to maintain data integrity.  
- All user inputs are validated before processing.  

## Dependencies
- **Python 3.x**  
- **No external packages required**  

## Notes
- Ensure **write permissions** in the program directory for JSON and CSV files.  
- **Backup data files** regularly.  
- **Do not modify JSON/CSV files manually** while the program is running.  


