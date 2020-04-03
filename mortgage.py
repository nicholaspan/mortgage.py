### Helper functions
def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monhtly payment for a mortage
       based off of loan size (loan), interest rate (r),
       and number of months (m)"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, ann_rate, months):
        """ Assumes: loan and ann_rate are floats, months is an int
            Creates a new mortgage of size loan, duration months, and
            annual interest rate ann_rate"""
        self.loan = loan
        self.rate = ann_rate / 12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None # description of the mortgage

    def make_payment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - (self.oustanding[-1] * self.rate)
        self.outstanding.append(self.outstanding[-1] - reduction)

    def get_total_paid(self):
        """Determine total amount paid thus far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend
        
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