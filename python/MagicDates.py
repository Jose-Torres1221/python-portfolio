#Introduction to Magic Dates
print("Welcome to Jose's Magic Date Emporium \n")
print('Give us a date and we will test it for magic! \n')

#Getting the date
Day = int(input('First the day (Number): '))
Month = int(input('Next the month (Number): '))
Year = int(input('And finally the last two digits of the year: '))

print('Thank you! Let us see what magic lies here!')

#Behind the scenes "magic"
product = Day * Month

if product == Year:
	print('You have chosen a magical date!')
else:
	print('Sorry my friend, no magic here!')
