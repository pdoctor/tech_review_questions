# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#  I should just be able to gather prime factors for this
# so from 1 to 10 my prime factors are 2, 2, 2, 3, 3, 5, 7 = 2520 roger

# good thing I already wrote a function to give me prime factors!

import problem3
from itertools import groupby

def find_smallest_common_multiple_of(number):
    prime_and_frequency = {}
    for x in xrange(2, number + 1):
        list_of_primes = problem3.get_prime_factors(x)

        # itertools lets us groupby on our list since it's already ordered
        for prime, group in groupby(list_of_primes):
            # okay so now we have each prime and how many times it's in our list, let's check our accumulated count
            # if we already have at least that many of the prime factor, ignore it, otherwise update our count
            frequency = len(list(group))
            if prime not in prime_and_frequency:
                prime_and_frequency[prime] = frequency
            elif prime_and_frequency[prime] > frequency:
                prime_and_frequency[prime] = frequency

    # now we have a dict of each prime and their frequency, we can iterate over it to reach out output
    smallest_number = 1
    for prime, frequency in prime_and_frequency.iteritems():
        smallest_number *= prime ** frequency

    return smallest_number

print find_smallest_common_multiple_of(20)

