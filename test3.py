def askuserforkilometers():
    userkilometers = float( input("Please enter the distance" + \
                                  " in kilometers: "))
    return userkilometers

def convertkilometerstomiles(userkilometers):
    miles = userkilometers * 0.6214
    return miles

def main():
    userkilometerstyped = askuserforkilometers()
    convertedmiles = convertkilometerstomiles( userkilometerstyped )

    print( userkilometerstyped, "kilometers converted to miles is", \
           convertedmiles, "miles" )
main()
