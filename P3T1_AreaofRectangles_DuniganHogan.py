# CTI-110 
# P3T1- Area of Rectangles 
# Ciera Dunigan-Hogan
# 07 March 2019
#

#Input the length and width of both rectangles.
#Calculate the area of both rectangles.
#Diplay which rectangle has the greater area.

choice = 'yes'
while choice.lower() == 'yes':

#Input
    width1 = int(input('Enter the width of the first rectangle: '))
    length1 = int(input('Enter the length of the first rectangle: '))
    width2 = int(input('Enter the width of the second rectangle: '))
    length2 = int(input('Enter the length of the second rectangle: '))


#Calculations
    area1 = width1 * length1
    area2 = width2 * length2

    if area1 > area2:
        print('Rectangle one has the greater area.')

    elif area2 > area1:
        print('Rectangle two has the greater area.')
        
    elif area1 == area2:
        print('The rectangles have the same area.')


choice = input("Do you want to run the program again?" +
               "Enter yes or no.")
        
