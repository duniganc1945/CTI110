#Find total profit from total projected sales.
# 19 February 2019
# CTI-110 P2T1 - Sales Prediction
# Ciera Dunigan-Hogan
#

##Find variables- annual23, sales, and profit.
##Input the projectedSales.
##Calculate the 23% or .23 profit.
##Display totalProfit. 

#Get total projected sales
sales = float(input("Enter total projected sales: "))

#Calaculate projected profit
profit = float(sales * .23)

#Display projected profit
print('Your projected profit is $', format(profit, ',.2f'), '.',
      sep= '')
