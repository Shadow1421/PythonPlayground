# Create a small command-line program in Python to Calculate the total invoice amount for the below purchases - 
# Book - Introduction to Python Programming: Rs 499.00
# Book - Python Libraries Cookbook: Rs. 855.00
# Book - Data Science in Python: Rs. 645.00
# - Taxes and additional charges are described as details - 
# GST: 12%
# Delivery Charges: Rs. 250.00
# Purchase details
book1_price = 499.00
book2_price = 855.00
book3_price = 645.00
gst_percentage = 12
delivery_charges = 250.00

# Calculate subtotal
subtotal = book1_price + book2_price + book3_price

# Calculate GST amount
gst_amount = (gst_percentage / 100) * subtotal

# Calculate total amount including GST and delivery charges
total_amount = subtotal + gst_amount + delivery_charges

# Print invoice details
print("Invoice Details:")
print("--------------")
print("Subtotal: Rs.", subtotal)
print("GST (", gst_percentage, "%): Rs.", gst_amount)
print("Delivery Charges: Rs.", delivery_charges)
print("Total Amount: Rs.", total_amount)
