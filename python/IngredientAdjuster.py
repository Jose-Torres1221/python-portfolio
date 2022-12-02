#Aquiring Cookie Amount
print("Welcome to Jose's Bakery!")
cookie_amt = int(input('How many cookies for today? '))


#Getting the percentage
percentage_change = cookie_amt / 48

#Applying percentage to ingredients
amt_sugar = 1.5 * percentage_change
amt_butter = 1 * percentage_change
amt_flour = 2.75 * percentage_change

#Printing everything
print(f'For your cookies you will use \n {amt_sugar:.1f} cups of sugar, \n {amt_butter:.1f} cups of butter, \n {amt_flour:.1f} cups of flour')
