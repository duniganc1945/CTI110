#P5T2 - Feet to Inches
#CTI-110
#Ciera DuniganHogan
#19 April 2019
#
choice = 'yes'
while choice.lower() == 'yes' :


    def main():
#Get input
        feet = int(input('Enter measurement in feet: '))
#Display conversion
        conversion (feet)

    def conversion (feet) :
#Calculate feet to inches
        inches = feet * 12

        print(inches, 'inches is equal to', feet , 'feet.')

    main()
    
        
    choice = input("Do you want to run the program again?" +
                   " Enter yes or no. ")                   
