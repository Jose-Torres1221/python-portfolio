#Intro to problem
print("Hello welcome to Jose's Wi-Fi Fixer \n")
print('Please answer with uppercase for the first letter! \n')

#Starting Troubleshooting
print('Reboot the computer and try to connect.')
Ans = input('Did that fix the problem? ')

if Ans == 'Yes':  #End First Branch
	print('Have a great day')
elif Ans == 'No':  #First Branch
	print('Reboot the router and try to connect')
	Ans = input('Did that fix the problem? ')
	if Ans == 'Yes':  #End Second Branch
		print('Have a great day!')
	elif Ans == 'No':  #Second Branch
		print('Make sure the cables between the router and modem are plugged in firmly.')
		Ans = input('Did that fix the problem? ')
		if Ans == 'Yes':  #End Third Branch
			print('Have a great day')
		elif Ans == 'No':  #Third Branch
			print('Move the router to a new location and try to connect.')
			Ans = input('Did that fix the problem? ')
			if Ans == 'Yes':  #End Final Branch
				print('Have a great day')
			elif Ans == 'No':
				print('Get a new router.')
