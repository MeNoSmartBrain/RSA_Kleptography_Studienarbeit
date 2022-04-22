import key
import attackUtil
import rsaUtil


def main():
    k_attacker = key.Key(32)
    #k_attacker.create_key()
    k_attacker.set_key_params(77839, 102701, 7993962600, 7994143139, 257, 5070100793)


    #print("--TEST--")
    #print(k_attacker)
    #msg = 2658547813
    #print("Message: ", msg)
    #cipher = rsaUtil.encrypt(msg, k_attacker.E, k_attacker.N)
    #print("Cipher: ",cipher)
    #decipher = rsaUtil.decrypt(cipher, k_attacker.D, k_attacker.N)
    #assert msg == decipher






    k_user = key.Key(64)

    #k_user.set_key_params(2658547813, 949493803, 2524274669814661224, 2524274673422702839, 17, 1187893962265722929)
    k_user.create_klepto_key(k_attacker.E, k_attacker.N)

    #print(k_user)


    attack = attackUtil.AttackUtil(k_attacker, k_user.E, k_user.N, k_user.rsa_bit_len)
    #print(attack.attack())





failure = 0
success = 0
for i in range(0,1000000):
    try:
        main()
        success += 1
    except RuntimeError:
        failure += 1

print("Success:",success)
print("Failure:",failure)
