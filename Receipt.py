# Setting description and prices on the furniture
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_setee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

# initializing the sales tax
sales_tax = 0.088 # 8.8%

customer_one_total = 0
customer_one_itemization = ""

# Customer one decides to purchase Lovely Loveseat
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description

# Calculating customer's total with tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
# Customer One Receipt
print("Customer One Items: " + customer_one_itemization)
print("Customer One Total: $" + str(customer_one_total))

# End of Customer One.

customer_two_total = 0
customer_two_itemization = ""

customer_two_total += stylish_setee_price + luxurious_lamp_price
customer_two_itemization += stylish_settee_description + luxurious_lamp_description

# Calculating customer's total with tax
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax
# Customer One Receipt
print("-------------------------------------------------------")
print("Customer Two Items: " + customer_two_itemization)
print("Customer Two Total: $" + str(customer_two_total))