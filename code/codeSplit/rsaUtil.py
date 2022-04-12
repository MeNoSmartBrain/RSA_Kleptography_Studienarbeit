def calc_n(P, Q):
    return P * Q


def calc_phi_n(P, Q):
    return (P - 1) * (Q - 1)


def modular_multiplicative_inverse(E, phiN):
    return pow(E, -1, phiN)


def to_binary(dec):
    return "{0:b}".format(dec)


def to_decimal(binary):
    return int(binary, 2)


def concatenate_in_binary(prev, tail, rsa_bit_len):
    key_bit_len = int(rsa_bit_len / 2)
    prev = to_binary(prev)
    tail = to_binary(tail)

    prev = "0" * (key_bit_len - len(prev)) + prev
    tail = "0" * (key_bit_len - len(tail)) + tail

    return to_decimal(prev + tail)


def split_in_binary(binary, rsa_bit_len):
    key_bit_len = int(rsa_bit_len/2)
    binary = to_binary(binary)
    binary = "0" * (key_bit_len * 2 - len(binary)) + binary
    prev = binary[:len(binary) // 2]
    tail = binary[len(binary) // 2:]
    return to_decimal(prev), to_decimal(tail)


def sign(msg, D, N):
    return pow(msg, D, N)


def encrypt(msg, E, N):
    return pow(msg, E, N)


def decrypt(cipher, D, N):
    return pow(cipher, D, N)
