#Aquiring all the Information
print('Thank you for choosing Bank of Jose!')
P = float(input('Please input how much you would like to deposit today:$ ')) #P is the original amount deposited

    
r = float(input('Please input the annual interest rate: '))
r = r / 100 #Percentage is given, divide by 100 to use properly

#Times interest is compounded
try:
	n = float(input('How many times is the interest compounded: '))
except ValueError:
	print('Input is not a number!')

#Aquiring for how many years
t = float(input('How many years will it be: '))


print('Thank you! Processing compound interest!')

#Preparing Results 
nt = n * t
A = P * (1 + r / n) ** nt

print(f'After {t} years, your account will amass to ${A:.2f}.')
