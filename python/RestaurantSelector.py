#Creating the list, also I changed Joe's to Jose's because I love burgers
Restaurants = ['Sunny Pizza', 'Corner Cafe', "Mama Fu's", "Jose's Burgers",'The Clay Pit']

#Asking the Questions
Vegetarian = input('Is someone in the group vegetarian? (Y/N): ')

Vegan = input('Is someone in the group vegan? (Y/N): ')

gluten_Free = input('Is someone in the group gluten-free? (Y/N): ')

#Filtering
if Vegetarian == 'Y':
	Restaurants.remove("Jose's Burgers")
elif Vegan == 'Y':
	Restaurants.remove('Sunny Pizza')
	Restaurants.remove("Mama Fu's")
	Restaurants.remove("Jose's Burgers")
elif gluten_Free == 'Y':
	Restaurants.remove("Mama Fu's")
	Restaurants.remove("Jose's Burgers")

#Printing Results
print('Your restaurant choices are:')
print(*Restaurants, sep='\n')

#Currently Being Reworked
