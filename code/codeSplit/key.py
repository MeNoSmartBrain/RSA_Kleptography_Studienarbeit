import math

import prime
import rsaUtil


class Key:

    def __init__(self, rsa_bit_len, opt_bit_limit=0):
        self.rsa_bit_len = rsa_bit_len
        self.key_bit_len = rsa_bit_len / 2
        self.opt_bit_limit = opt_bit_limit
        self.D = None
        self.E = None
        self.N = None
        self.PhiN = None
        self.Q = None
        self.P = None
        self.prime = prime.Prime(rsa_bit_len)

    def create_key(self):
        created = False
        while not created:
            try:
                P = self.prime.gen_prime()
                Q = self.prime.gen_prime()

                PhiN = rsaUtil.calc_phi_n(P, Q)
                N = rsaUtil.calc_n(P, Q)

                E = prime.fermat_prime()
                D = rsaUtil.modular_multiplicative_inverse(E, PhiN)

                self.set_key_params(P, Q, PhiN, N, E, D)
                created = True

            except ValueError:
                print("Trying to generate key failed. Trying again ...")

        print("Key successfully generated!")

    def create_klepto_key(self, attacker_E, attacker_N):
        created = False
        while not created:
            P = self.prime.gen_prime_with_opt(self.opt_bit_limit)
            vP = rsaUtil.encrypt(P, attacker_E, attacker_N)

            min_bit_construct_Q = rsaUtil.concatenate_in_binary((vP - 1), 0, self.rsa_bit_len)
            max_bit_construct_Q = rsaUtil.concatenate_in_binary(vP, int(pow(2, self.key_bit_len) - 2), self.rsa_bit_len)

            lower_bound_Q = math.ceil(min_bit_construct_Q / P)
            upper_bound_Q = math.floor(max_bit_construct_Q / P)

            try:
                Q = int(prime.gen_prime_in_bounds(lower_bound_Q, upper_bound_Q))
                created = True
                #print(vP)
            except (ValueError, TypeError):
                #print("Margin to small")
                pass

        PhiN = rsaUtil.calc_phi_n(P, Q)
        N = rsaUtil.calc_n(P, Q)

        #print("True:", rsaUtil.to_binary(vP))
        #print("True:", rsaUtil.to_binary(N))

        created = False
        while not created:
            try:
                E = prime.fermat_prime()
                D = rsaUtil.modular_multiplicative_inverse(E, PhiN)
                created = True
            except ValueError:
                pass
                #print("Trying to generate Key failed. Trying again ...")
        #print("User Key successfully generated!")

        self.set_key_params(P, Q, PhiN, N, E, D)

    def set_key_params(self, P, Q, PhiN, N, E, D):
        self.P = P
        self.Q = Q
        self.PhiN = PhiN
        self.N = N
        self.E = E
        self.D = D

    def __str__(self):
        return str({
            "P": self.P,
            "Q": self.Q,
            "PhiN": self.PhiN,
            "N": self.N,
            "E": self.E,
            "D": self.D,
        })
