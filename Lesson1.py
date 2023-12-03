################# Time Value

# Time Value of money = concept that money today is worth more than money in the future
# Future value = value of asset in future based on growth rate over time
#     -  $1000 today can be invested to become $1100 in the future. This is the premium we will get
#     -  inflation means buying power today is more than future

## Discrete model
# FV = PV (1+r) ^ n     PV = present value, n = duration in years, r = interest
# higher n = higher risk = expects higher reward

## Continuous model
# x(t + dt) - x(t) = dx(t)/dt * dt
# As this is proportional to r and x(t):
#           dx(t)/dt * dt = r * x(t) * dt
#           dx(t)/dt * dt = r * x(t) * dt => integrate
#           x(t)          = x(0) e^(r * t)
#           FV            = PV e^(r * t)
# Taylors/Maclaurins series is about taking non-polynomials, and trying to approximate them to polynomials around certain inputs. Easier to deal with/differentiate
# Using Taylor's series https://www.youtube.com/watch?v=kZf6phY418U&ab_channel=ExamSolutions we derive the differential equation above

from math import exp

def discrete_future_val(x, r, n):
    return x*(1 + r)**n

def discrete_present_val(y, r, n):
    return y*(1 + r)**-n

def continuous_future_val(x, r, t):
    return x * exp(r*t)

def discrete_present_val(y, r, t):
    return y*exp(-r*t)

if __name__ == '__main__':
    x = 100
    r = 0.05
    n = 5

    print("$100 before 5 years with 5% interest = ", discrete_future_val(100, 0.05, 5))
    print("$100 after 5 years with 5% interest = ", discrete_present_val(100, 0.05, 5))
    print("$100 before time t with 5% interest = ", continuous_future_val(100, 0.05, 5))
    print("$100 after time t with 5% interest = ", discrete_present_val(100, 0.05, 5))

############### Stocks
# Shares = unit of stock
# Companies <-> Stock exchange lists all company stocks, there exists several (NYSE, NASDAC) <-> Brokers/broker firms can buy/sell shares <-> Investors
# Realizing stock = selling stock
# Stock divideneds are paid to shareholders on regular basis

# Volatility
# Standard deviation or variance between same security

############### Commodities
# Physical assets e.g. oil, gold
# Commodities prices typically rise along with inflation - very useful
# Commodities are extremly volatile, so must use futures
# Future contracts = avoid market volatility
# Pairs trading strategy - typically positive correlation between commodity and company reliant on commodity e.g. gold and gold mine. Can invest in company instead

############### FOREX Market
# Currency market
# Lower exchange rate = stronger currency e.g $1 <-> £0.9       GBP is stronger
# Factors that impact exchange rate
#       Interest rate - higher interst, more investment in country's bank, more demand for currency, higher
#       Money Supply - more money printed, higher inflation, lower demand, lower
#       Financial stability/economic growth of country

# Arbitratge = riskless money
# Construct directed graph with nodes V (currencies), edges E (relative value)
# Take negative natural log -ln(x) of edges. All values > 1 => negative value. Gives you graph where negative cycles = arbitrage loop
# e.g £1 -> $1.05 -> €1.25
#           -ln(1.05) = -0.05
#           -ln(1.25) = -0.22
#           converting from GPB -> $ -> € should give us risk-free profit
# Can use shortest path algorithm to find arbitrage loops

############### Positions
# Long = you own that stock. Expect stock value to increase. Buy at time t0, sell at tn
# Short = you sell that stock. Expect stock value to decrease. Sell at time t0, buy at tn
#       Short selling = borrow stock, sell them immediately, buy back in future, return stocks to lender and pocket the difference
# Short = much riskier than long
#       Long = maximum loss of 100% the amount you invest
#       Short = maximum loss unlimited depending on how much price increases instead of decreases

# Bear market = security prices fall
# Bull market = security prices rise
