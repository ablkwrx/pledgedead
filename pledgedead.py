#!/usr/bin/env python3

# Dont rent, buy, squat, couchsurf, nothing is safe anymore. Stay at your rents if you can.

years = 30
value = 200000
loan = 100000
apr = 1.1

# Dont talk shit about Total https://www.youtube.com/watch?v=C-M8mfBAaBs
total = (loan*apr)

# Check inflation. Hard coded very conservatively for now (early 2022). This feature needs to be included.
inflation = 20

# Loop through all years to determine when to stop paying the insane rates and start investing instead. 7+ probably, at that point just buy shares in gamestop.
year = 0
while year < (years):
    year = (year+1)
    if year < (years):
        for month in range (12):
            # Calculate our equity %
            # Calculate our interest %
            # Calculate if it no longer makes sense to apply money to the equity.
            print (month)
