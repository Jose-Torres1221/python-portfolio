N = 30
total = 0  # accumulator
# loop over fractions to print and calculate total
for numerator in range(1, N+1):
	denominator = N+1 - numerator 
	ending = ' + '
	if numerator == N:  # check for detecting the last term in series
		ending = ' = '
	print(f'{numerator}/{denominator}', end=ending)
	total += numerator/denominator

# display total
print(f'{total:.2f}')  
