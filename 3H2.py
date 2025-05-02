# −*− coding: utf−8 −*−
"""
Created on Fri Fev 8 04:10:44 2024

@author: Mario Ramalho
Edited by: Miguel Pascoal
"""
def main():
    print("This program calculates the future value\n", "of an investment for the duration you wish to know in years")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate in perecents: "))
    year = eval(input("Enter the length of investment in years: "))
    for i in range (year):
        principal = principal * (1 + (apr * .01))
        print(f"The value in {i+1} years is: {principal:.2f}")
        #I put .2f so it only shows 2 decimal places, since money is presented in cents

main()
