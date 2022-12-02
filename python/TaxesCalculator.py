#Aquiring Prices
print('Welcome to JoseMart!')
first_Item = float(input('Please input 1st item price: '))
second_Item = float(input('Please input 2nd item price: '))
third_Item = float(input('Please input 3rd item price: '))
fourth_Item = float(input('Please input 4th item price: '))
fifth_Item = float(input('Please input 5th item price: '))
print('Thank you!')

#Taxes time
subtotal = first_Item + second_Item + third_Item + fourth_Item + fifth_Item
taxes = subtotal * 0.07
total = subtotal + taxes

#Printing everything
print(f'Subtotal: {subtotal:.2f}')
print(f'Taxes: {taxes:.2f}')
print(f'Total: {total:.2f}')
