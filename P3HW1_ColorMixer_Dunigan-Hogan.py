#CTI-110
#P3HW1-Color Mixer
#Ciera Dunigan-Hogan
#07 March 2019
#

#Input color one and color two, either red, blue, or yellow.
#Calculate or "mix" the two colors.
#Display the outcome.

choice = 'yes'
while choice.lower() == 'yes' :

#Input
    pc1 = input( "Please enter primary color 1: " )
    pc2 = input( "Please enter primary color 2: " )

#Calculations and output
    if ( pc1.lower() == "red" and pc2.lower() == "blue" ) or \
       ( pc1.lower() == "blue" and pc2.lower() == "red" ) :
        print( pc1 + " mixed with " + pc2 + " makes purple.")
    elif ( pc1.lower() == "red" and pc2.lower() == "yellow" ) or \
         ( pc1.lower() == "yellow" and pc2.lower() == "red" ) :
        print( pc1 + " mixed with " + pc2.lower() + " makes orange.")
    elif ( pc1.lower() == "yellow" and pc2.lower() == "blue" ) or \
         ( pc1.lower() == "blue" and pc2.lower() == "yellow" ) :
        print( pc1 + " mixed with " + pc2 + " makes green.")
    else:
        print('ERROR: You did not enter primary colors!')

    
choice = input("Do you want to run the program again?" +
               "Enter yes or no.")
