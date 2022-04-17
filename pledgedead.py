#!/usr/bin/env python3

# Dont rent, buy, squat, couchsurf, nothing is safe anymore. Stay at your rents if you can.

# How much do you have left after paying the minimum that you are willin to put towards the mortgage, or invest?
monthly_extra_cash = 2500

# How much do you expect every month on an external investment? 10% in this case.
expected_investment_value = 1.1

# How many years is the mortgage?
global years
years = 30

# How much is the current valuation of the house?
value = 159000
# Down payment, in this case 20%
down_payment = (value*.2)

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


while year < (years):
    year = (year+1)
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
            #print(loan)
    print("Year",year)
    print("Acquired equity: "+"${:.0f}".format(total_equity));
    print("Interest Payments: "+"${:.0f}".format(total_interest_loss));
    print("Remaining Loan: "+"${:.0f}".format(loan));
