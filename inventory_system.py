"""Inventory management system for adding, removing, saving, and loading stock data."""

import json
from datetime import datetime
from ast import literal_eval

# Global inventory data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to the stock."""
    if logs is None:
        logs = []

    if not item or not isinstance(qty, (int, float)):
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specified quantity of an item from the stock."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")


def get_qty(item):
    """Return the current quantity of a specified item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print("Error reading JSON file. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(stock_data, indent=4))
    except OSError as e:
        print(f"Error saving file: {e}")


def print_data():
    """Print the current inventory data."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantities below the specified threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution function for testing the inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, 10)  # Corrected invalid type for qty
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

    # Removed unsafe eval usage
    literal_eval("('safe', 'literal', 'evaluation')")


if __name__ == "__main__":
    main()
