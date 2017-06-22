'''
Name: Tim Lowrance
ID:
Due Date: 26 June 2017
Date Submitted:
Description: This is a calculator to track purchase and sale of stock by
    investors. The program will query and process user input and display
    calculated totals
'''

# Static commission rate
COMMISSION_RATE = 0.03

# Purchases Section
print("PURCHASE OF STOCK")
# Get information for Stock purchases
purchase_broker = input("Enter name of investor: ")
shares_purchased = int(
    input("Enter number of shares purchased (as a whole amount): "))
price_per_share = float(input("Enter the cost per share (in dollars): "))

# Calculate the amount and commission from provided information
purchase_amount = shares_purchased * price_per_share
purchase_commission = purchase_amount * COMMISSION_RATE

# display the information
print("Purchase amount is $", format(purchase_amount, ',.2f'), sep='')
print("Commission for the purchase is $", format(
    purchase_commission, ',.2f'), sep='')

# Sales section
print("SALE OF STOCK")
# Get information for Stock purchases
sale_broker = input("Enter name of investor: ")
shares_sold = int(
    input("Enter number of shares sold (as a whole amount): "))
cost_per_share = float(input("Enter the cost per share (in dollars): "))


# Calculate the amount and commission from provided information
sale_amount = shares_sold * cost_per_share
sale_commission = sale_amount * COMMISSION_RATE

# display the information
print("Sale amount is $", format(sale_amount, ',.2f'), sep='')
print("Commission for the sale is $", format(sale_commission, ',.2f'), sep='')


# summary Section
print("SUMMARY OF TRANSACTIONS")

# calculate the summary totals
total_commission = purchase_commission + sale_commission


profit_loss_total = sale_amount - \
    (shares_sold * price_per_share) - total_commission

print("Investor name is " + sale_broker)
print("Total commission in $", format(total_commission, ',.2f'), sep='')
print("Profit/Loss amount is $", format(profit_loss_total, ',.2f'), sep='')
