def convert_to_kilograms ( x ) :
    value = (x / 1000)
    return value


num = int ( input ( "Enter a number to convert:" ) )
result = convert_to_kilograms ( num )
print ( str ( num ) + " g is " + str ( result ) + " kg" )
