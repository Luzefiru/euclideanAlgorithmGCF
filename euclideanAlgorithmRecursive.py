def euclideanGCF(a, b):
    """
    
    Input
    -----
    a, b (int) : Non-negative, non-zero integers

    Output
    ------
    (int) : This function returns the greatest common factor (GCF) of the two inputs.
    
    """

    # checks the numbers if they can be operated on
    if a < 1 or b < 1: raise ValueError("Cannot execute algorithm for these numbers. Please use non-negaitve & non-zero integers.")

    # checks if a is bigger than b, otherwise swaps a & b
    if a < b: a,b = b,a

    # calculates for the remainder
    r = a % b

    # base case: if remainder is 0, the modulo divisor in the equation is the GCF. if it goes under 0, there is no GCF.
    if r == 0: return b
    elif r < 0: raise ValueError("There is no GCF for the inputted numbers.")
    
    # recursive call
    return euclideanGCF(b, r)

def __main__():
    a, b = int(input("Input a positive integer: ")), int(input("Input another posiive integer: "))
    print(f"The GFC is: {euclideanGCF(a, b)}")

__main__()