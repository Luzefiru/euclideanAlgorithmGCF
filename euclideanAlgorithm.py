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
    if a < 1 or b < 1: return "Cannot execute algorithm for these numbers."

    # checks if a is bigger than b, otherwise swaps a & b
    if a < b: a,b = b,a
    r = None

    # keep doing the Euclidean Algorithm until the resulting remainder is 0
    while r != 0:
        r = a % b
        if r == 0: break
        a, b = b, r
    
    # returns the GCF of the algorithm, which is the modulo divisor (smaller number) to get a remainder of 0
    return b

def __main__():
    a, b = int(input("Input a positive integer: ")), int(input("Input another posiive integer: "))
    print(f"The GFC is: {euclideanGCF(a, b)}")

__main__()