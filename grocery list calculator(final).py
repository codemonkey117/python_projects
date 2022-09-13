print('Hello! Welcome to the grocery pricing calculator.')

grocery_list = dict()

keep_going = True
while keep_going:
    user_input = input('Please enter product and price, or press Q/q to quit: ')
    if (user_input == 'Q' or user_input == 'q'):
        keep_going = False
    else:
        product,price = user_input.split()
        grocery_list.update({product: float(price)})

print("Here's your grocery list:")

subtotal = 0.0

total_g_tax = 4.5 / 100    #this expression is to be factored as a percentage for grocery tax.
tulsa_s_tax = 8.517 / 100   #this expression is to be factored as a percentage for tulsa sales tax. 

for product, price in grocery_list.items():
    print(product, ' $', price)
    subtotal += price

total_tax = subtotal * (total_g_tax + tulsa_s_tax)
grocery_tax = subtotal * (total_g_tax)
total_full_tax = subtotal + total_tax
total_only_g_tax = subtotal + grocery_tax

print(f'Subtotal ${subtotal:.2f},\nTotal tax ${total_tax:.2f},\nGrocery Tax ${grocery_tax:.2f}, \nTotal full tax ${total_full_tax:.2f}, \nTotal without state tax ${total_only_g_tax:.2f}')



    
    
  