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

class Fixed(Mortgage):
    """Subclass of Mortgage to track fixed mortgage objects"""
    def __init__(self):
        pass

    pass

class FixedWithPts(Mortgage):
    """Subclass of Mortgage to track mortgage with points objects"""
    def __init__(self):
        pass
    
    pass

class TwoRate(Mortgage):
    """Subclass of Mortgage to track variable interest rate mortgage"""
    def __init__(self):
        pass

    pass