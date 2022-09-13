print('Hello! Welcome to the Canadian dollar to dodgecoin translator:')
print('Please enter a value in Canadian Dollars to be translated to DodgeCoin, (press q to quit)')
 
user_input = input('Enter monetary value here:  ')

keep_going = True

dollar_amount = user_input

conversions = 0

def canadian_dollar_to_dodgecoin(dollar_amount):
    dodge_coin_amount = float(dollar_amount) * 5.71
    return dodge_coin_amount 
while keep_going:  
    if user_input == 'q':
        keep_going = False
    else:
        dollars_in_dodge_coin = float(canadian_dollar_to_dodgecoin(dollar_amount))
        print(f'{dollar_amount} Canadian Dollars is {dollars_in_dodge_coin:.2f} DodgeCoin')
        conversions += 1
        user_input = input('Please enter a value in pounds sterling to be converted into etherium (press q to quit) ')
        dollar_amount = user_input
print('you have coverted', conversions, 'times')
    

         

        