#!/usr/bin/python3.8
import sys
import pandas as pd
import cpi
from datetime import date

# Enter your yearly salary here before taxes
salary =

# Enter your rent per month here.
rent =

yearly_rent = (rent*12)
base_tax = 4807.50
bonus_tax_base = (salary-41775)
bonus_tax = (bonus_tax_base*.22)
tax = (base_tax+bonus_tax)
new_salary = (salary-tax)

inflation = cpi.inflate(80000, date(2021, 1, 1), to=date(2022, 3, 1))
inflation_impact = (inflation-salary)
new_salary_inflation = (new_salary-inflation_impact)
salary_after_rent = (new_salary_inflation-yearly_rent)
print('This year, the government has taken, or will be taking $%d from your salary.' %tax)
print('What you are left with, is $%d' %new_salary)
print('Based on the U.S. Bureau of Labor Statistics, you have lost $%d via inflation in the past year out of the 10 months of data 2 months ago that they have available.' %inflation_impact)
print('The remaining effective value of the money you have acquired over the past year is $%d' %new_salary_inflation)
print('After deducting your rent, you are left with $%d for other expenses' %salary_after_rent)
