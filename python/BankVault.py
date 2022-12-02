#Introduction
print("Thank you for choosing Jose's Bank!\n")
print("To access your bank vault just answer the following questions!")

#Setting correct answers
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
correct_Pin = '1883'
correct_Password = 'longhorn'

#Collecting Answers
date = input('What day is it today: ')
time = int(input('What time is it? (Military time 0-23): '))
pin_Code = input('Please enter the 4-digit pincode: ')
password = input('Finally enter the password: ')

#Checking Answers
factor_One = date in days_of_the_week
if factor_One == True:
	if time < 16 and time > 9:
		if pin_Code == correct_Pin or password == correct_Password:
			print('Open')
		else:
			print('Do not open')
	else:
		print('Do not open')
else:
	print('Do not open')
