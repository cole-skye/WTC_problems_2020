import sys
from user.authentication import*
from transactions.journal import*
import banking


if __name__ in '__main__':
    """
    This for loop is for prints out all arguments called when running the function.
    """
    for i in sys.argv[1:]:
        print(i)
    """
    Calls respected packages and modules in order to be printed out.
    """
    authenticate_user()
    receive_income(100)
    pay_expense(100)
    banking.do_reconciliation()
    # help("modules")
