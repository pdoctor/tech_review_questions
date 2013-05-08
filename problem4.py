# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# I've tried a few times, but I can't think of a better way than brute force for this at the moment

def is_palindrome(x):
    """ checks if the number as a string and its reversal are the same
    """
    return str(x) == str(x)[::-1]


def find_greatest_palindrome(start_range, end_range):
    """ given a starting and ending point, will find the largest palindrome number between them
        raises ValueError if none are found.
    """
    max_found = 0
    for first_multiple in xrange(start_range, end_range):
        for second_multiple in xrange(first_multiple, end_range):
            product = first_multiple * second_multiple
            if is_palindrome(product) and product > max_found:
                max_found = product

    if max_found == 0:
        raise ValueError("Specified range contains no palindrome numbers.")
    else:
        return max_found

print find_greatest_palindrome(100, 1000)

