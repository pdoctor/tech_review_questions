# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# So the easy solution is like this but I think I can do better below:
import timeit


def get_next_prime():
    n = 2
    prime_numbers = set()
    while True:
        for prime in prime_numbers:
            if n % prime == 0:
                break
        else:
            prime_numbers.add(n)
            yield n

        n += 1


def find_sequence_of_primes_numbered(seq_number):
    prime_number_generator = get_next_prime()
    for x in xrange(seq_number - 1):
        next(prime_number_generator)

    print next(prime_number_generator)

timer = timeit.Timer("find_sequence_of_primes_numbered(10001)", "from __main__ import find_sequence_of_primes_numbered")
print timer.timeit(1)

# I keep reading about Sieves, so I thought I'd try a simple Sieve of Eratosthenes instead
# ahah! but now we have a problem, so the Sieve is intended to stop at maximum number X
# but instead we want the Yth prime number in the prime number sequence, but we have
# no idea how big that will be.  I can instead "grow" the Sieve as needed, but that's an
# expensive operation, however I don't see a better way at the moment, so this,
# while fun to code, may be the wrong solution to the problem

# So for each number between 1 and X will have an index from 0 to X-1 in this array
# in the index's location we'll have a bool which represents if this number is prime or not
# we'll start by initializing them all to true, then ruling them out as we go
prime_seq_number = 10001
current_sieve_size = 1000000
is_index_prime = [True] * current_sieve_size
is_index_prime[0] = False    # by definition, 1 is not prime

for number in xrange(1, current_sieve_size):
    if is_index_prime[number]:
        for multiple in xrange(number, prime_seq_number/number):
            if multiple * number < prime_seq_number:
                pass


