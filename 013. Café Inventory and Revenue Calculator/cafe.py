# TASK 2

# Create a list of items sold in the café.
menu = ['Coffee', 'Cake', 'Bread', 'Muffin']

# Create a dictionary to know the stock quantity of each item.
stock = {
    'Coffee': 2,
    'Cake': 3,
    'Bread': 1,
    'Muffin': 7
    }

# Create a dictionary to have the prices for each menu item.
price = {
    'Coffee': 2.50,
    'Cake': 3.00,
    'Bread': 2.75,
    'Muffin': 3.25
}

# Set the default value of the total stock as 0.
total_stock = 0

# Use a loop to iterate through the menu items and
# calculate the total value based on stock quantities and prices.
for index, item in enumerate(menu):
    item_value = (stock[item] * price[item])
    total_stock += item_value

# Print out the calculated total stock value 39.5.
print(total_stock)