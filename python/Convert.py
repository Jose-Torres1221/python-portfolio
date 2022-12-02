def get_input():
    #prompt user for units
    unit = input('Please specify Pounds or Kilograms: ')
    unit = unit.capitalize()
    while unit not in {'Pounds', 'Kilograms'}:
        print('Please input Pounds or Kilograms')
        unit = input('Please specify Pounds or Kilograms: ')
        unit = unit.capitalize()  
        
    #prompt user for weight    
    Weight = int(input('Enter weight of object/person: '))
    while Weight < 0: #Extra credit
        print('Weight cannot be negative')
        Weight = int(input('Enter weight of object/person: ')) 
    #return both
    return unit, Weight
    
def convert_to_pounds(kilograms):
    conversion_factor = 2.205
    Weight = kilograms*conversion_factor
    final_Unit = 'Pounds'
    return Weight, final_Unit


def convert_to_kilograms(pounds):
    # see convert_to_pounds above, but converting in the other direction
    conversion_factor = 2.205
    Weight = pounds/conversion_factor
    final_Unit = 'Kilograms'
    return Weight, final_Unit

def display_output(Weight, final_Unit):
    print(f'{Weight:,.1f} {final_Unit}')

def main():
    unit, Weight = get_input()
     
    if unit == 'Pounds':
        Weight, final_Unit = convert_to_kilograms(Weight)
        display_output(Weight, final_Unit)
    else:
        Weight, final_Unit = convert_to_pounds(Weight)
        display_output(Weight,final_Unit)
		
main()
