"""
Functions for anuity calculation
"""
import itertools
import functools


MONTHS_IN_YEAR = 12
TO_PERCENTAGE = 0.01
FLOAT_EPS = 1*10**-9


def get_mortage_interest(n: int, p: float, r: float, x: float) -> float:
    """
    :param n: number of months
    :param p: principal
    :param r: fixed interest rate monthly
    :param x: monthly payment
    """
    if n <= 0:
        raise ValueError(f'Number of years has to be positive: {n}.')
    if r < 0:
        raise ValueError(f'Fixed interest rate can not be negative: {r}.')
    if abs(r) < FLOAT_EPS:
        return 0
    return get_remaining_principal(n = n-1, p=p, r=r, x=x)*r

def get_remaining_principal(n: int, p: float, r: float, x: float) -> float:
    """
    :param n: number of months
    :param p: principal
    :param r: fixed interest rate monthly
    :param x: monthly payment
    """
    if n == 0:
        return p
    if n < 0:
        raise ValueError(f'Number of years has to be positive: {n}.')
    if r < 0:
        raise ValueError(f'Fixed interest rate can not be negative: {r}.')
    if abs(r) < FLOAT_EPS:
        return p - p/n
    return p*(1+r)**(n) - x*(((1+r)**n - 1)/r)

def get_monthly_payment(n: int, p: float, r: float) -> float:
    """
    :param n: number of years
    :param p: principal
    :param r: fixed interest rate monthly
    """
    if n <= 0:
        raise ValueError(f'Number of years has to be positive: {n}.')
    if r < 0:
        raise ValueError(f'Fixed interest rate can not be negative: {r}.')
    # r ~= 0
    if abs(r) < FLOAT_EPS:
        return p/(MONTHS_IN_YEAR*n)
    return p*r*((1+r)**(MONTHS_IN_YEAR*n))/(((1+r)**(MONTHS_IN_YEAR*n))-1)


def calculate_monthly_payment(interest_rate: float, loan_years: int, principal_amount: int):
    ir = float(interest_rate)
    n = int(loan_years)
    principal = float(principal_amount)
    r = (ir*TO_PERCENTAGE)/MONTHS_IN_YEAR
    return get_monthly_payment(n=n, p=principal, r=r)


def calculate_mortgage(interest_rate: float, loan_years: int, principal_amount: int):
    """
    # I1 = P0*r
    # P1 = P0 - (X - I1)
    # P1 = P0 - (X - P0*r)
    # P1 = P0*(1+r) - X
    # I2 = P1*r = (P0*(1+r) - X)*(r) = P0*(1+r)*r-X*r
    # P2 = P1 - (X - I2) = P0*(1+r) - X - (X-(P0*(1+r)*r-X*r)) = P0*(1+r) + P0*(1+r)*r - X -X + X*r
    # = p*(1+r)*(1+r) - X*(1 + (1 + r))
    # In = P2*r = [p*(1+r)*(1+r) - X*(1 + (1 + r))]*r
    # Pn = P0*(1+r)^n - X*(1 + (1+r) + .. + (1+r)^(n-1)) = P0*(1+r)^n - X*((1+r)^n -1)/(1+r-1)
    # Pn => 0 <==> X = P0*r*(1+r)^n/((1+r)^n-1)
    """

    ir = float(interest_rate)
    n = int(loan_years)
    principal = float(principal_amount)
    r = (ir*TO_PERCENTAGE)/MONTHS_IN_YEAR
    # print(f'{r =}, {principal =}, {n =}')

    years = list(range(1, n+1))
    months = list(range(1, MONTHS_IN_YEAR+1))
    # print('Monthly payment')
    x = get_monthly_payment(n=n, p=principal, r=r)
    # print(x)

    # print('remaining_principal')
    remaining_principal = [get_remaining_principal(n=i*MONTHS_IN_YEAR, p=principal, r=r, x=x)
                           for i in years]
    # print(remaining_principal)

    # print('total_interest')
    current_interest = [functools.reduce(
        lambda x, y: x+y, (get_mortage_interest(n=m + MONTHS_IN_YEAR*(i-1), p=principal, r=r, x=x)
                           for m in months)) for i in years]

    interest_paid_term = list(itertools.accumulate(current_interest, lambda x, y: x+y))

    remaining_principal = list(map(lambda x: x if x > 0 else 0, remaining_principal))
    interest_paid_term = list(map(lambda x: x if x > 0 else 0, interest_paid_term))

    return years, remaining_principal, interest_paid_term
