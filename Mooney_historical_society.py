print("Welcome to the Mooney historical society, please enter a selection from the following years.")
print("Select from the following: 1415, 1607, 1776, 1861, 1917, 1920, 1945")

user_input = int(input('Type a 4 digit number: '))

if user_input == 1415:
    print("On october 25, 1415; \nThe battle of Agincourt took place.\nThis battle was a significant victory for the english in the 100 years war against France,\nmarking a time when their influence increased immensly as an imperialist society.")

elif user_input == 1607:
    print("On may 14, 1607; \nJamestown was founded, in what was later known as the state of Virginia. \nThis marked the first English colony to be established in the United States.")

elif user_input == 1776:
    print("On two dates in 1776, July 4th and August 2, \nMembers of the american colonial government signed the declaration of independence.\nThe declaration was taken as a declaration of war by the English king and government.\nThis led to The American revolutionary war.")

elif user_input == 1861:
    print("On April 12th 1861, \nConfederacy forces fire on Fort Sumter in North Carolina, at 4:30 AM.\nLess than 36 hours later, the fort surrendered.\nThis marked the beginning of the American Civil War.")

elif user_input == 1917:
    print("On april 6th, 1917,\nAfter numerous sunken US merchant vessels and civilian casualties abroad, \nCongress voted unanimously to declare war on germany.\nThis marked the official beginning of The US , Militaries involvment in WWI, \nbarring the american volunteer force that had been fighting alongside the French since 1914.")

elif user_input == 1920:
    print("On august 18th, 1920,\nThe womens sufferagists movement had garnered enough support in congress to be granted the inaliable right to vote,\nmarking a new turning point in American social policy. \nThis type of political momentum led to inspiring many more movements throughout the 20th century.")

elif user_input == 1945:
    print("On may 8th, 1945, \nThe allied forces in Europe declare victory over germany. \nthis marked the end of WWII in Europe.")
else:
    print("Sorry, this date is either not logged or hasn't happened yet.")

print("To enter a new date, please re-run the program and enter a different value.")