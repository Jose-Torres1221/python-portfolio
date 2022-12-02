# YOUR SOLUTION GOES HERE
print("Welcome to Jose's leap year predictor!")

#Aquiring the year
user_Year = int(input('Enter a year: '))

#Math Time
if user_Year % 100 == 0:
	if user_Year % 400 == 0:
		print(f'In {user_Year} February has 29 days!')
	else:
		print(f'In {user_Year} February has 28 days!')
elif user_Year % 4 == 0:
	print(f'In {user_Year} February has 29 days!')
else:
	print(f'In {user_Year} February has 28 days!')
