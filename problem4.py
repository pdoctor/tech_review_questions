# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# so that's from 100*100 = 10,000 to 999 * 999 = 998001
# 997799

def find_max_range(number_of_digits):
    """ given how many digits we have to work with, this finds
        the maximum range, for example a 3 digit solution
        can be no larger than 999 * 999 = 998001 """
    return (9 * number_of_digits) ** 2

def find_max_palindrome(number_to_search_below):
    string_version = str(number_to_search_below)
    number_length = len(string_version)
    if number_length % 2 == 0:
        palindrome_number = string_version[0:number_length/2] + string_version[number_length/2 -1 ::-1]
        print palindrome_number
    else:
        palindrome_number = string_version[0:number_length/2 + 1] + string_version[number_length/2 ::-1]
        print palindrome_number

find_max_palindrome(1234567)