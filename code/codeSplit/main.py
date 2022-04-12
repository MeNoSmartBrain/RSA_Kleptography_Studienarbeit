import key
import attackUtil
import rsaUtil


def main():
    k_attacker = key.Key(32)
    k_attacker.create_key()
    print(k_attacker)

    k_user = key.Key(64)
    k_user.create_klepto_key(k_attacker.E, k_attacker.N)
    print(k_user)

    attack = attackUtil.AttackUtil(k_attacker, k_user.E, k_user.N, k_user.rsa_bit_len)
    print(attack.attack())






main()
