print("Hello! Welcome to the team roster list!")

roster = []

keep_going = True

while keep_going:
    user_input = input(str('Please enter a player to add to the list. Press quit to display the current roster:  '))
    if user_input == 'quit':
        keep_going = False
        print("Current Roster is: ")
    else:
        roster.append(str(user_input))

for name in range(len(roster)):
    print((roster[name]), end="\n")


print('Thank you! Laters Gators!')