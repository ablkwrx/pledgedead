#!/usr/bin/env python3

# Stay at your rents as long as you can and invest all your money and retire at 30.
# Set your variables:

# How many years is the mortgage?
years = 30

# How much is the current valuation of the house?
value = 300000

# What % are you putting forth as a down payment? In this case, it is set to .2, or 20%
down_payment = (value*.2)

# How much do you have left after paying the minimum that you are willing to put towards the investment?
monthly_extra_cash = 2000

# How much do you expect every month on an external investment? 7% in this case.
expected_annual_investment_percent = 7

# The % APR. Disregard points here. This is the raw APR %. In this case, we are getting a 5.75% APR.
rate = .05750


# End User Variables.





# Every year, the amount of extra cash you have.
yearly_extra_cash = (monthly_extra_cash*12)

# The grand total extra cash you have to invest for the longevity of the mortgage total. So for a 10 year loan, $1 every month is $12 a month, times 10 for $120 total.
mortgage_extra_cash = (yearly_extra_cash*years)

# Turning this into a decimal to multiply as a percentage.
expected_annual_investment_decimal = (expected_annual_investment_percent/100)

# Figure out the loan.
global loan
loan = (value-down_payment)

# Yearly payments for the house. Here, we are paying the minimum for it and putting what we have left towards the investment.
yearly_payment=(loan/years)

# Monthly payments for house. Here, we are paying the minimum for it and putting what we have left towards the investment.
monthly = (yearly_payment/12)

# TODO: Inflation?

# Set the vars as 0 to begin the loop.
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


# While the year 0 is less than years which is defined at the top, add 1 year, to indicate a year is passing. Calculate the yearly investment gains by multiplying the investments for the entire year by the expected yearly investment gain to add to the interest and compound on itself next year.
while year < (years):
    year = (year+1)
    yearly_investment_gains = (investment*expected_annual_investment_decimal)
    total_investment_gains = (yearly_investment_gains+yearly_investment_gains)
    investment = (investment+yearly_investment_gains)
    # Here, we are looking if it is the current year (for example, 0 > 0+1, then looping through each month)
    if year < (years+1):
        # For every month of this year, multiply the APR against the loan amount to calculate the
        for month in range (12):
            # The secret sauce. You need to multiply the apr against the outstanding loan balance. Set amoritize to the yearly amount paid towards interest and divide it by 12. This is the interest you pay every month. Your equity is the monthly payment minus interest, as interest is paid before equity.
            amoritize = (rate*loan)
            int(amoritize)
            interest = (amoritize/12)
            int(interest)
            # Regardless of the payment, interest takes precedent over equity when paying the minimum. This lessens as the loan decreases in size.
            equity = (monthly-interest)
            int(equity)
            # Your new equity is your total_equity. This excludes the downpayment equity you have. This script only cares about the loan, and the investment.
            total_equity = (total_equity+equity)
            int(total_equity)
            #Interest losses are calculated by adding the interest paid this month to the total loss variable.
            total_interest_loss = (total_interest_loss+interest)
            int(total_interest_loss)
            #Now that we paid this month, we take the loan we got, and subtract the equity from it. This reduces the interest payment next month.
            loan = (loan-equity)
            int(loan)
            # Here, we invest. If this is the first month, we are adding out monthly extra cash to the investment, This gets added every single month.
            investment = (investment + monthly_extra_cash)

print("Summary")
print("Paid every single month for the mortgage length in years for investment account:",monthly_extra_cash)
print("Acquired equity after finishing the mortgage: "+"${:.0f}".format(value));
print("Mortgage Interest Payments: "+"${:.0f}".format(total_interest_loss));
print("Investment payments: "+"${:.0f}".format(mortgage_extra_cash));
print("Interest gains: "+"${:.0f}".format(total_investment_gains));
print("Investment account funds after the mortgage is complete: "+"${:.0f}".format(investment));
print("Remaining Loan: 0");
