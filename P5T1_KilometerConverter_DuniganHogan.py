#P5T1- Kilometer Converter
#CTI-110
#Ciera Dunigan-Hogan
#19 April 2019
#

#Write a program the convert kilometers to miles. Get input,
#distance in kilometers, for user. Calculate input and convert to
#miles. Display(output) the distance in miles.



choice = 'yes'
while choice.lower() == 'yes' :


    def main():
#Input from user
        km = int(input('Enter distace in kilometers: '))

#Display conversion
        conversion (km)

    def conversion (km) :
#Calculate distance
        miles = km * .6214

        print( km , 'kilometers is', format(miles, '.3f') ,'miles.' )
#Call main
    main()

    choice = input("Do you want to run the program again?" +
                   " Enter yes or no. ")

