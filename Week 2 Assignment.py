"""Program: Week 2 Assignment.py
Author:Felix Ortiz
Compute tax based on gross income
1. User input field
    Name
    Gross Income
    State Tax Rate
2. Calculations
    Federal Tax
    FICA Tax
    State Tax
    Estimate Tax
3. The outputs are
        Name:
        Gross Income:
        State Income Tax Rate
        Estimated tax is based on a gross income of"""

# Request for Input
name = (input("Enter your name: "))
grossIncome = (input("Enter your gross income: "))
Taxrate = float(input("Enter state tax rate: "))

# Calculation
federalTax = (float(str(grossIncome))) * .0945
Ficatax = (float(str(grossIncome))) * .0765
stateTax = ((float(grossIncome)) * (float(Taxrate)))
Estimatetax = federalTax + Ficatax + stateTax
taxEstimate = round(Estimatetax, 2)

#Total Output Display
print (str(name) + "'s estimated tax is $" + str(Estimatetax) + " based on a gross income of $" + str(grossIncome))