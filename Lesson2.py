############### Bonds
# investor loans money to entity (government/company) for fixed interest rate - fixed income
# unlike stocks
#   bonds are a debt entity (lend money that is repaid) while stocks are entity ownership
#   bonds are impacted by interest rate, stocks are not

# Market interest rate and bond prices are negatively correlated - higher interest rate = more profitable to lend money to banks than buy bonds

# Yield to Maturity
# 1) zero coupon bonds
#       1000$, 2 years, 10% interest
#       1000$ = principal amount/par value/face value/nominal value = only cash amount paid back to investor upon maturity
#       10% interest = premium
# Present value = x / (1 + r)^n = current value that investor pays
#   x: principal amount, r: MARKET interest rate, n: maturity time
# 2) coupon bonds
#       $1000, 10% coupon, 2 years
#       coupon rate = 10% = paid annually on principal amount
# Present value of each COUPON payment = c / (1 + r)^n
# Present value of coupon & PRINCIPAL amount = sum[ c / (1 + r)^i ] + x / (1 + r)^n
#                                   = c * sum[ 1 / (1 + r)^i ] + x / (1 + r)^n
#                                   = c/r * [1 - 1/(1 + r)^n] + x / (1 + r)^n     convert to closed form

# We can calculate the present value using the discrete formula
#       PV of principal amount = x * e ^ -y(T - t)  y: YTM, t: current time, T: maturity time
#       PV of coupon amount = sum [ci * e^ -y * (ti - t)]
# Yield = return of a bond = annual coupon amount/bond price (how much paid at t = 0)
# Yield to maturity (y) = overall interest rate

# Macauley duration = how long it takes for a bond to be repaid from its cash flows
# Modified duration = how sensitive the bond price is to market interest changes
#                   = -1/V * dV/dy
#                     V: bond price, y: yield to maturity
# For zero coupon bonds, the Macauley duration = T (maturity)
# Prefer longer maturity when interest rates are expected to fall
# Prefer shorter maturity when interest rates are expected to rise/remain stable

# Risks
#   interest risk (changes in interest rate)
#   default risk (bond issues unable to issue principal/coupon payments on time)
#   inflation risk (cash flow value varies)

class ZeroCouponbond:

    def __init__(self, principal, maturity, interest):
        self.principal = principal
        self.maturity = maturity
        self.interest = interest

    def calculatePresentValue(self):
        return self.principal / (1 + self.interest)**self.maturity
class CouponBond:

    def __init__(self, principal, b_interest, m_interest, maturity):
        self.principal = principal
        self.maturity = maturity
        self.b_interest = b_interest # bond interest rate
        self.m_interest = m_interest # market interest rate
        self.coupon = b_interest * principal

    def calculatePresentValue(self):
        # c/r * [1 - 1/(1 + r)^n]
        couponPresentPrice = (self.coupon / self.m_interest) * (1 - 1/(1 + self.m_interest)**self.maturity)
        # x / (1 + r)^n
        principalPresentPrice = self.principal / (1 + self.m_interest)**self.maturity
        return principalPresentPrice + couponPresentPrice

    def calculatePresentValueSummation(self):
        couponPresentPrice = 0

        # c * sum[ 1 / (1 + r)^i ]
        for t in range(1, self.maturity + 1):
            couponPresentPrice += 1/(1 + self.m_interest)**t

        # x / (1 + r)^n
        principalPresentPrice = self.principal / (1 + self.m_interest)**self.maturity
        return principalPresentPrice + self.coupon * couponPresentPrice

if __name__ == '__main__':
    zeroCoupBond = ZeroCouponbond(1000, 2, 0.04)
    coupBond = CouponBond(1000, 0.1, 0.04, 3)
    print("present price of zero coupon bond = %.2f" % zeroCoupBond.calculatePresentValue())
    print("present price of coupon bond = %.2f" % coupBond.calculatePresentValue())
    print("present price summation of coupon bond = %.2f" % coupBond.calculatePresentValueSummation())
