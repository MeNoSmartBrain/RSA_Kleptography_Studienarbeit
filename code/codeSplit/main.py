import key
import attackUtil
import rsa


def main():
    # Choose bits for the user key
    nbits = int(input("Enter the number of bits for the key: "))
    public_e = int(input("Enter the public exponent: "))
    public_n = int(input("Enter the public modulus: "))

    for key_member in attack_key_list:
        if key_member['bits'] == (nbits // 2):
            attack_key_params = key_member
            break
    else:
        raise ValueError("Unsupported key size")

    k_attacker = key.Key(nbits // 2)

    k_attacker.set_key_params(attack_key_params['P'],
                              attack_key_params['Q'],
                              attack_key_params['PhiN'],
                              attack_key_params['N'],
                              attack_key_params['E'],
                              attack_key_params['D'])

    print("Used attacker key: ", attack_key_params)

    attack = attackUtil.AttackUtil(k_attacker, public_e, public_n, nbits)
    extracted_key = attack.attack()
    print("Extracted key: ", extracted_key)
    print("-------------------------------------------------------")
    print("P: ", extracted_key.P)
    print("Q: ", extracted_key.Q)


def automized():
    def print_private_key(private_key):
        print("Private Key: " + str({
            'n': private_key.n,
            'e': private_key.e,
            'd': private_key.d,
            'p': private_key.p,
            'q': private_key.q,
        }))

    nbits = 1024

    keyPair = rsa.newkeys(nbits)

    publicKey = keyPair[0]
    privateKey = keyPair[1]

    print("P:", privateKey.p)
    print("Q:", privateKey.q)
    print_private_key(privateKey)

    print("-------------------------------------------------------")
    print("Public-Key: ")
    print("E:", publicKey.e)
    public_e = publicKey.e
    print("N:", publicKey.n)
    public_n = publicKey.n

    for key_member in attack_key_list:
        if key_member['bits'] == (nbits // 2):
            attack_key_params = key_member
            break
    else:
        raise ValueError("Unsupported key size")

    k_attacker = key.Key(nbits // 2)

    k_attacker.set_key_params(attack_key_params['P'],
                              attack_key_params['Q'],
                              attack_key_params['PhiN'],
                              attack_key_params['N'],
                              attack_key_params['E'],
                              attack_key_params['D'])

    print("Used attacker key: ", attack_key_params)

    attack = attackUtil.AttackUtil(k_attacker, public_e, public_n, nbits)
    extracted_key = attack.attack()
    print("Extracted key: ", extracted_key)
    print("-------------------------------------------------------")
    print("P: ", extracted_key.P)
    print("Q: ", extracted_key.Q)


"""
    RSA-32 attack key for RSA-64
    """
attack_key_32bit = {
    "bits": 32,
    'P': 55711,
    'Q': 52267,
    'PhiN': 2911738860,
    'N': 2911846837,
    'E': 65537,
    'D': 2586563513
}

"""
RSA-64 attack key for RSA-128
"""
attack_key_64bit = {
    "bits": 64,
    'P': 3337805567,
    'Q': 3588638527,
    'PhiN': 11978177646444835716,
    'N': 11978177653371279809,
    'E': 65537,
    'D': 8251686289907860337
}

"""
RSA-128 attack key for RSA-256
"""
attack_key_128bit = {
    "bits": 128,
    'P': 17710801766177235259,
    'Q': 18091019263583148667,
    'PhiN': 320406455925414815348297473514270865828,
    'N': 320406455925414815384099294544031249753,
    'E': 65537,
    'D': 160640788086077788161105305167034074025
}

"""
RSA-256 attack key for RSA-512
"""
attack_key_256bit = {
    "bits": 256,
    'P': 311834484718983040923434328875130419489,
    'Q': 280759999968508389541262383721162977537,
    'PhiN': 87550649919881508449292040460081073471619892660407524730411434762294800621568,
    'N': 87550649919881508449292040460081073472212487145095016160876131474891094018593,
    'E': 65537,
    'D': 25562379819291891056612344083550533910301763066006957683696580621275172954113
}

"""
RSA-512 attack key for RSA-1024
"""
attack_key_512bit = {
    "bits": 512,
    'P': 112521994437407179228272509629412919599626512438638105699093501210820894593209,
    'Q': 112312641839220091086236058767510201946622681626557939895724731547562130414781,
    'PhiN': 12637642460283227912453427505123163135385844433426130935431593592393193879763212235182688166468690541994487432970259166074458051017260751234746672410814240,
    'N': 12637642460283227912453427505123163135385844433426130935431593592393193879763437069818964793739005050562884356091805415268523247062855569467505055435822229,
    'E': 65537,
    'D': 9369715536951066485590003242045478077244887331128609825787282491636560883435227161870803027430515181279462660299142360491904064863034620176333076162190273
}

"""
RSA-1024 attack key for RSA-2048
"""
attack_key_1024bit = {
    "bits": 1024,
    'P': 10081224188957022301369160794101677390103605266976431077002272822605198833460224389043488474819151791614188031102770976493881841598831624467814532665199817,
    'Q': 10912393816780377847987697353894222310894402031155781470821277861509951590001725191894398643501768690820944951211877059131726109706753776272723728711673879,
    'PhiN': 110010288505151389688894719277185522828409459771793674436630705338808661328726157700088971193337370193429742426770117155309860123615943909904163096586189248558616551985256752304284256202232154499974386367719130320805375053519280218715277607383864030785774730698978983489801451581875567585540331034476697606448,
    'N': 110010288505151389688894719277185522828409459771793674436630705338808661328726157700088971193337370193429742426770117155309860123615943909904163096586189269552234557722656901661142404198131855497981684499931678144356059168669703680664858545270982351706257165831961298137837077189826873170941071572738074480143,
    'E': 65537,
    'D': 60677966780356324434657770609452710365157775788192894754647401263213993464925052238320584260749794127776650277597177089737717987525659405453647368896921875534383189971513207536128710395628239328395778238557015469680832162513007024217157559114880403204971008213782936283158259788846575477701327284347218595265
}
attack_key_list = [attack_key_32bit, attack_key_64bit, attack_key_128bit, attack_key_256bit, attack_key_512bit,
                   attack_key_1024bit]
# main()
automized()

# failure = 0
# success = 0
# for i in range(0,10000):
#     try:
#         main()
#         success += 1
#     except RuntimeError:
#         failure += 1
#
# print("Success:",success)
# print("Failure:",failure)


# 32 bit for 64
# k_attacker.set_key_params(55711, 52267, 2911738860, 2911846837, 65537, 2586563513)
# 64 bit for 128
# k_attacker.set_key_params(3337805567, 3588638527, 11978177646444835716, 11978177653371279809, 65537, 8251686289907860337)
# 128 bit for 256
# k_attacker.set_key_params(  17710801766177235259,
#                             18091019263583148667,
#                             320406455925414815348297473514270865828,
#                             320406455925414815384099294544031249753,
#                             65537,
#                             160640788086077788161105305167034074025)
# 256 bit for 512
# k_attacker.set_key_params(  311834484718983040923434328875130419489,
#                             280759999968508389541262383721162977537,
#                             87550649919881508449292040460081073471619892660407524730411434762294800621568,
#                             87550649919881508449292040460081073472212487145095016160876131474891094018593,
#                             65537,
#                             25562379819291891056612344083550533910301763066006957683696580621275172954113
#                             )
# 512 bit for 1024
# k_attacker.set_key_params(  112521994437407179228272509629412919599626512438638105699093501210820894593209,
#                             112312641839220091086236058767510201946622681626557939895724731547562130414781,
#                             12637642460283227912453427505123163135385844433426130935431593592393193879763212235182688166468690541994487432970259166074458051017260751234746672410814240,
#                             12637642460283227912453427505123163135385844433426130935431593592393193879763437069818964793739005050562884356091805415268523247062855569467505055435822229,
#                             65537,
#                             9369715536951066485590003242045478077244887331128609825787282491636560883435227161870803027430515181279462660299142360491904064863034620176333076162190273
#                             )
# 1024 bit for 2048
# k_attacker.set_key_params(
#     10081224188957022301369160794101677390103605266976431077002272822605198833460224389043488474819151791614188031102770976493881841598831624467814532665199817,
#     10912393816780377847987697353894222310894402031155781470821277861509951590001725191894398643501768690820944951211877059131726109706753776272723728711673879,
#     110010288505151389688894719277185522828409459771793674436630705338808661328726157700088971193337370193429742426770117155309860123615943909904163096586189248558616551985256752304284256202232154499974386367719130320805375053519280218715277607383864030785774730698978983489801451581875567585540331034476697606448,
#     110010288505151389688894719277185522828409459771793674436630705338808661328726157700088971193337370193429742426770117155309860123615943909904163096586189269552234557722656901661142404198131855497981684499931678144356059168669703680664858545270982351706257165831961298137837077189826873170941071572738074480143,
#     65537,
#     60677966780356324434657770609452710365157775788192894754647401263213993464925052238320584260749794127776650277597177089737717987525659405453647368896921875534383189971513207536128710395628239328395778238557015469680832162513007024217157559114880403204971008213782936283158259788846575477701327284347218595265
# )

# p, q = 2594285323613304725109257241747646966790862657043067420635492062696025985706551327811442143111403273902355211789429312877808173049529392518256444518940464436178270804033349495341770406585855439570612317645848055448785393463034146473680410857705493250605758328852071230649974807542351024562424907068298080689480967558849454821784328785401803263606564766736483305532628045323523409160262894629180823717653583726099017137711170128815700013670199682856397361984587461, 6831923273884704650532102160104890840101868415337168165612923719355121434163040669063725033794766306160432606165658779366187140479300425182380943215788199
# k_user.create_key_given_p_q(min(p, q), max(p, q))
