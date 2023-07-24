###Azubi store has product that customers love. Below are the products, prices and the number of customers that purchased products last week.
#The owner wants you to do some culculations on the data with these criteria's: 
#1. calculate the total price average for all products 2.
#create a new price list that reduces the old prices by $ 5 
#3. calculate the total revenue generated from the product 
#4. calculate the average daily revenue generated from the products 
#5. based on the new prices, which products are less than $ 30below is the data you are to use for the problem: prices = [30, 25, 40, 20, 20, 35, 45, 50, 35] last week = [2, 3, 5, 8, 4, 4, 6, 2, 9] kindly solve this problem using python programming*SOLUTION* #Product detailsproducts = ["Sankofa Foods", "James Town Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Maka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
# Calculate the total price average for all products
 
products = ["Sankofa Foods", "James Town Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Maka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35] 
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#calculate total price average for all products
Total_price = sum(prices) 
Average_price = Total_price / len(products)
print("Average price for all products:$",Average_price)

#Create a new price list that reduces the old prices by $5 
new_prices = [price - 5 for price in prices]
print("New price list:", new_prices)

# Calculate the total revenue generated from the products

total_revenue = sum(price * customers for price, customers in zip(prices, last_week))
print("Total revenue generated: $", total_revenue)

#Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / 7 

# Assuming 7 days in a week
print("Average daily revenue generated: $", average_daily_revenue)

#Find products with prices less than $30 based on new prices
less_than_30 = [product for product, price in zip(products, new_prices) if price < 30]
print("Products with prices less than $30:", less_than_30)
