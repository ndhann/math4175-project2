#!/usr/bin/env python3
from array import *
import string
import numpy

ciphertext = "XSIPICTVEQQRGHJUYEXVVISEEFRXRLRPAVEPLPIELLFPGAQZBXEIPXBIVZXQGGBRRXTIYBFPVFCNGHDIOYEBXJSRXUHWPATSZPIDIDZRBRCIOIAMQZRFLFASHIHIEPISEHIBGEYIIWPTPPWQIAFETREXEXEXTDSQNGEWMRQLICZUGRLHPWUKAXHTRMANRXSEFKVOIDYEIELWZPQGBGXCSXSIXVLGOIFLXZXTIVKHLXMEFTVPWGPGEEHIZJBKGPQQRGBWDSYIGBQPWGRNUPPXAVRVSGIDXUXGZRFIAMSQIXIPMVZRUGPHQXYZMPTXTSZWSKSXXTIGXGSRAPBZCAVAZVWICIHIABRCIETBGWPXAEPHYCXAVQXVZVPYYREFXTSEBDPHIEEKEYXUWFNIOFKESXHPVMPWNHRIRSEXBLQBPRFEYCOSZFYYMOEGBSYWEIEOMNIERBPIYGDCCMGPVFEVGGZQYYABGLXUSALFJHQJNNPEAUXUMLPOQCAXGPWEEERXZHQGERTEXTIPHQXYZMPTXTSZWFHPPPKMAMLPLMRQLSQXTIRGHFWQVGAMDEBTYBIDFAXUPLPRFLRWEEEUWVGQZXUSAHZPVQPRVXCSZMPGIEAAVXLSCEFVRLXZRMRREINXDSABGOIHMPXMQXTIPHQXYZMPTXTSZWCKSGMPIEBWDIDZRWATXTEJTVCEZXFXIVMZKGASDIOSZFYYMOEGBSYWFLRIVZZUHRKGLRZSGIVZZUHRMLPHMXNUINEGWRBXSEEHRLMRRQHGAIEIOLAHPZKKWHVLELMXVMGLRZSGUILGOIFLIOFKEARXSMDHCTVECIIQHRZXTEIXEYCEMYOICFGPYXXDEZHGAIOMEGHLWTSZWJBXSMZXUXIIIOYGBZPFDEAVLLVQWGBPWSZKBBRRATMYXXSIDIUTWYSFCRMFPIZEQXGTWUSAPLPXTIEMSDIQOYXKTWXEGBSYAQQHLXHSDOJBXSGARTKIDWURQNWEVKEPTHPQUGFIVTZMGLZVZYBWNGHZXTIELXZGDESMEYEBTEHENLFLNMEOHDIFLIDEXPBYXSIYYYMMAPQGBFTPXURTVSYGQVALXSEFLNOIMIQRGAIQSOYFHJDSYYPAHPFMXRUYEAQGNGEWPMKEXIELMXJXATPXRRXHZRSSVGKSSZIFMEYHURSHVXIPTHUPTGPIOTXPENSHMLZANIFMXZTDSGXGEPUFRKXJEZHFXGFVUXLBRMSFLBNVWEIWNGHZYDXRVLYSXSTR"

m6 = ["", "", "", "", "", ""]
m7 = ["", "", "", "", "", "", ""]
m8 = ["", "", "", "", "", "", "", ""]

for i in range(6):
    m6[i] = ciphertext[i::6]

for i in range(7):
    m7[i] = ciphertext[i::7]

for i in range(8):
    m8[i] = ciphertext[i::8]

i6 = []
i7 = []
i8 = []

for j in range(6):
    icx = 0
    for k in string.ascii_uppercase:
        icx = icx + (m6[j].count(k) * (m6[j].count(k) - 1))
    icx = icx / (len(m6[j]) * (len(m6[j]) - 1))
    i6.append(icx)

for j in range(7):
    icx = 0
    for k in string.ascii_uppercase:
        icx = icx + (m7[j].count(k) * (m7[j].count(k) - 1))
    icx = icx / (len(m7[j]) * (len(m7[j]) - 1))
    i7.append(icx)

for j in range(8):
    icx = 0
    for k in string.ascii_uppercase:
        icx = icx + (m8[j].count(k) * (m8[j].count(k) - 1))
    icx = icx / (len(m8[j]) * (len(m8[j]) - 1))
    i8.append(icx)

print("Index of coincidences for m = 6")
print(i6)
print("Index of coincidences for m = 7")
print(i7)
print("Index of coincidences for m = 8")
print(i8)

p_freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
key = []

for j in range(7):
    q7 = []
    vg = []
    mg = []
    for k in string.ascii_uppercase:
        q7.append(m7[j].count(k) / len(m7[j]))
    
    for i in range(26):
        vg.append(q7[i:] + q7[:i])
        mg.append(numpy.dot(vg[i], p_freq))
    
    maxval = 0
    index = 0
    for i in range(len(mg)):
        if (mg[i] > maxval):
            maxval = mg[i]
            index = i
    
    print(maxval)
    print(index)
    key.append(index)

print(key)
plaintext = []
asciibase = 65
for i in range(len(ciphertext)):
    temp = ord(ciphertext[i]) - asciibase
    temp = (temp - (key[i % len(key)])) % 26
    temp = chr(temp + asciibase)
    plaintext.append(temp)

print(''.join(plaintext))
