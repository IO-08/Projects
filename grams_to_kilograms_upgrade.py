def convert_to_kilograms(x):
    kg = (x / 1000)
    return kg
def convert_to_grams(y):
    g = (y *1000)
    return g
options = int(input("Would you like like to convert to Kilograms (KG) (1) or Grams (2):"))
if options == 1:
    num = int(input("Enter the number to convert to Kilograms :"))
    result = convert_to_kilograms(num)
    print (str( num ) + " g is " + str( result) + " kg")

elif options == 2:
    num = int(input("Enter the number to convert Grams:"))
    result = convert_to_grams(num)
    print(str(num) + " Kg is " + str(result) + " g")
