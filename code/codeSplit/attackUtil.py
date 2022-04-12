import rsaUtil
import key


class AttackUtil:

    def __init__(self, attackerKey, public_E, public_N, public_rsa_bit_len):
        self.D = None
        self.E = None
        self.N = None
        self.PhiN = None
        self.Q = None
        self.P = None
        self.vP2 = None
        self.vP1 = None
        self.public_N = public_N
        self.public_E = public_E
        self.attackerKey = attackerKey
        self.rsa_bit_len = public_rsa_bit_len

    def attack(self):
        self.extract_vP()
        self.get_prime_factors()
        self.calc_key_params()
        return self.return_params_as_key()

    def extract_vP(self):
        self.vP1 = rsaUtil.split_in_binary(self.public_N, self.rsa_bit_len)[0]
        self.vP2 = self.vP1 + 1

        print("Extracted:", self.vP1)
        # print("Extracted:", rsaUtil.to_binary(self.public_N))
        # print("Extracted:", rsaUtil.to_binary(self.vP1))
        # print("Extracted:", rsaUtil.to_binary(self.vP2))

    def get_prime_factors(self):
        P1 = rsaUtil.decrypt(self.vP1, self.attackerKey.D, self.attackerKey.N)
        P2 = rsaUtil.decrypt(self.vP2, self.attackerKey.D, self.attackerKey.N)

        Q1 = self.public_N / P1
        Q2 = self.public_N / P2

        if Q1.is_integer():
            self.P = P1
            self.Q = Q1
        elif not Q1.is_integer() and Q2.is_integer():
            self.P = P2
            self.Q = Q2
        else:
            print("Prime factors couldn't be recovered. Either non compromised publicKey or programming error!")
            raise

    def calc_key_params(self):
        self.PhiN = rsaUtil.calc_phi_n(self.P, self.Q)
        self.N = self.public_N

        created = False
        while not created:
            try:
                self.E = self.public_E
                self.D = rsaUtil.modular_multiplicative_inverse(self.E, self.PhiN)
                created = True
            except ValueError:
                print("Trying to generate Key failed. Trying again ...")
        print("User Key successfully generated!")

    def return_params_as_key(self):
        ret_key = key.Key(self.rsa_bit_len)
        ret_key.set_key_params(self.P, self.Q, self.PhiN, self.N, self.E, self.D)

        return ret_key
