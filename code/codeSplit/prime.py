import sympy
import random


def gen_prime_in_bounds(lower_bound, upper_bound):
    return sympy.randprime(lower_bound, upper_bound)


def fermat_prime():
    i = random.randint(0, 4)
    return pow(2, pow(2, i)) + 1


class Prime:

    def __init__(self, rsa_bit_len, min_prime=0):
        self.key_bit_len = rsa_bit_len / 2
        self.MIN_PRIME = min_prime

    def gen_prime(self):
        return sympy.randprime(pow(2, self.MIN_PRIME), pow(2, self.key_bit_len))

    def gen_prime_with_opt(self, opt_bit_limit):
        return sympy.randprime(pow(2, self.MIN_PRIME), pow(2, self.key_bit_len - opt_bit_limit))
