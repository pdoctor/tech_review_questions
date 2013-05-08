# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#  I should just be able to gather prime factors for this
# so from 1 to 10 my prime factors are 2, 2, 2, 3, 3, 5, 7 = 2520 roger

# good thing I already wrote a function to give me prime factors!

import problem3

for x in xrange(2, 21):
    print problem3.get_prime_factors(x)

print problem3.get_prime_factors(8)