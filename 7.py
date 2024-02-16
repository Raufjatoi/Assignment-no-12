# 7. Restaurant Menu Parser:
# Write a program that reads a restaurant menu file (text or CSV) and stores items, prices, and 
# categories in a dictionary. Allow users to browse by category or search for specific items.
import pandas as pd

# Function to extract items, prices, and categories efficiently
def parse_menu_file(filepath):
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(filepath)

        # Create an empty dictionary to store menu items
        menu_items = {}

        # Iterate through each row (item) in the DataFrame
        for index, row in df.iterrows():
            # Extract item name, price, and category (assuming column names)
            item_name = row['Item Name']  # Adapt column names as needed
            price = row['Price']  # Adapt column names as needed
            category = row['Category']  # Adapt column names as needed

            # Convert price to a float and handle potential exceptions
            try:
                price = float(price.strip('$'))  # Remove leading/trailing dollar signs
            except ValueError:
                print(f"Warning: Invalid price format for item '{item_name}'. Skipping.")
                continue  # Skip items with invalid price format

            # Add item to the dictionary, handling cases where item name is not unique
            if item_name in menu_items:
                # Create a list of price and category pairs if multiple entries exist
                if isinstance(menu_items[item_name], float):
                    menu_items[item_name] = [menu_items[item_name], (price, category)]
                else:
                    menu_items[item_name].append((price, category))
            else:
                menu_items[item_name] = price  # Initial entry for single price

        return menu_items

    except FileNotFoundError:
        print(f"Error: Menu file '{filepath}' not found.")
        return None

# Get the menu items dictionary
menu_items = parse_menu_file("ras.csv")  # Replace with your actual file path

# User interaction loop
while True:
    print("\nRestaurant Menu:")
    print("1. Browse by Category")
    print("2. Search for Item")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        # Display categories (assuming unique category values)
        categories = set(menu_items.values() if isinstance(menu_items.values(), dict) else [])
        for category in categories:
            print(f"- {category}")

        selected_category = input("\nEnter category or 'b' to go back: ")
        if selected_category.lower() == 'b':
            continue

        # Filter items by category if selected
        if selected_category in categories:
            filtered_items = {item: price for item, price in menu_items.items() if (
                isinstance(price, float) and category == menu_items[item]) or (
                isinstance(price, list) and any(c[1] == selected_category for c in price))}
            print("\nItems in", selected_category, ":")
            for item, price in filtered_items.items():
                print(f"- {item}: ${price:.2f}")  # Format price with two decimal places
        else:
            print("Invalid category. Please try again.")

    elif choice == '2':
        search_term = input("\nEnter item name: ")
        search_results = {item: price for item, price in menu_items.items() if search_term.lower() in item.lower()}
        if search_results:
            print("\nSearch results:")
            for item, price in search_results.items():
                print(f"- {item}: ${price:.2f}")  # Format price with two decimal places
        else:
            print("Item not found.")

    elif choice == '3':
        print("\nExiting...")
        break

    else:
        print("Invalid choice. Please try again.")

