#!/usr/bin/env python3

# Dont rent, buy, squat, couchsurf, nothing is safe anymore. Stay at your rents if you can and invest all your money and retire at 20.

# Do you want to invest instead of paying down the equity?
invest = 1

# How many years is the mortgage?
years = 30

# How much is the current valuation of the house?
value = 159000

# Down payment, in this case 20%
down_payment = (value*.2)

# How much do you have left after paying the minimum that you are willin to put towards the mortgage, or invest?
monthly_extra_cash = 700
yearly_extra_cash = (monthly_extra_cash*12)
mortgage_extra_cash = (yearly_extra_cash*years)

# How much do you expect every month on an external investment? 10% in this case.
expected_annual_investment_percent = 10
expected_annual_investment_decimal = (expected_annual_investment_percent/100)

# Figure out the loan.
global loan
loan = (value-down_payment)

rate = .05750
monthly = 742.30
actual_monthly =  1097.63

# Dont talk shit about Total https://www.youtube.com/watch?v=C-M8mfBAaBs -- that was me writing this.
global total
total = (monthly*360)

# Check inflation. Hard coded very conservatively for now (early 2022). This feature needs to be included. TODO
#inflation = 20

# Loop through all years to determine when to stop paying the insane rates and start investing instead. 7+ probably, at that point just buy shares in gamestop.
year = 0
global total_interest_loss
total_interest_loss = 0
global total_equity
total_equity = 0
global investment
investment = 0
global investment_payments
investment_payments = 0
global investment_gain
investment_gain = 0
global investment_gains
investment_gains = 0
int(investment_gains)
global yearly_investment_gain
yearly_investment_gain = 0
global total_investment_gains
total_investment_gains = 0

while year < (years):
    year = (year+1)
    #print ("Year",year)
    yearly_investment_gains = (investment*expected_annual_investment_decimal)
    #print("yearly_investment_gains",yearly_investment_gains)
    investment = (investment+yearly_investment_gains)
    if year < (years+1):
        for month in range (12):
            # The secret sauce. You need to multiply the apr against the outstanding loan balance.
            amoritize = (rate*loan)
            int(amoritize)
            #print(amoritize)
            interest = (amoritize/12)
            int(interest)
            #print(interest)
            equity = (monthly-interest)
            int(equity)
            #print(equity)
            total_equity = (total_equity+equity)
            int(total_equity)
            #print(total_equity)
            total_interest_loss = (total_interest_loss+interest)
            int(total_interest_loss)
            #print(total_interest_loss)
            loan = (loan-equity)
            int(loan)
            investment = (investment + monthly_extra_cash)
total_investment_gains=(investment-mortgage_extra_cash)

print("Summary")
print("Paid every single month for 30 years for investment account:",monthly_extra_cash)
print("Acquired equity: "+"${:.0f}".format(total_equity));
print("Home Interest Payments: "+"${:.0f}".format(total_interest_loss));
print("Investment payments: "+"${:.0f}".format(mortgage_extra_cash));
print("Interest gains: "+"${:.0f}".format(total_investment_gains));
print("Investment account total: "+"${:.0f}".format(investment));
print("Remaining Loan: "+"${:.0f}".format(loan));
