### Helper functions
def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monhtly payment for a mortage
       based off of loan size (loan), interest rate (r),
       and number of months (m)"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self):
        pass

    pass