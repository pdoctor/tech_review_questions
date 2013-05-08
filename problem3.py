# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def get_prime_factors(number_to_factor):
    """ returns a list of prime factors for a given number
    """
    prime_factors = []
    while True:
        try:
            next_prime = return_smallest_prime_factor(number_to_factor)
        except ValueError:
            print 'An invalid input was specified'
            raise

        # add the number to our list of primes
        prime_factors.append(next_prime)
        # if it is equal to itself, we have found all prime factors (since the number itself is prime)
        if next_prime == number_to_factor:
            break

        # if we found a prime, we can divide it out before we continue our search
        number_to_factor /= next_prime



    return prime_factors


def return_smallest_prime_factor(number_to_factor):
    """ Finds the smallest factor of the given number.  Given that
        it is the smallest factor, it is also necessarily prime
    """

    # there is never a need to search beyond square root of the number, if we go beyond that then
    # the number is prime, plus one for inclusive generation in range
    stop_search_at = int(math.floor(math.sqrt(number_to_factor))) + 1

    # for each int up to when we stop iteration, start at 2 since 1 is not prime
    for test_number in xrange(2, stop_search_at):
        # if they evenly divide the number
        if number_to_factor % test_number == 0:
            # then return the number as a factor
            return test_number

    # this means no factors were found up to n/2, so the number must be prime (or we
    # were given bad input)
    return number_to_factor

#the_prime_factors_are = get_prime_factors(600851475143)
#print max(the_prime_factors_are)

