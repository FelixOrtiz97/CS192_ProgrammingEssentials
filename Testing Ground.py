grossIncome = 47250
Taxrate = .065



federalTax = str(grossIncome) * .945
Ficatax = str(grossIncome) * .765
stateTax = str(grossIncome) * str(Taxrate)
Estimatetax = federalTax + Ficatax + stateTax
taxEstimate = round(Estimatetax, 2)