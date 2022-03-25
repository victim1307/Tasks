from itertools import *
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
# the solution approach is i have a known string which is encrypted
# from and i know the partial key
# i just need to try brute forcing the 4 characters of the key and try bruteforcing
# i know the enc string and i can try bute forcing string the key
# next thought is to optmise the time complexity
# os i decrypted the enc string and i know and stored the decrypted values in a set and in dict with corresponding key
# next i have domne is encrypt the string and i know and store it in an other set and in dict with corresponding key
# mitm meet in the middle attack
# one loop from top and other from bottom
# the intersection 2 sets give a value and by dict we ccan get keys from dicts
# after knowing keys simple decryption
x = "0123456789abcdef"
y = "hel103245!@#"
set1 = {""}
set2 = {""}
dict1 = {"":""}
dict2 = {"":""}
def decrypt_aes(key,ciphertext):
    cipher = AES.new(key, mode=AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def encrypt_aes(key,plaintext):
    cipher = AES.new(key, mode=AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext,16))
    return ciphertext

pt = "manoharr"
ct = "0f57000d34320f747c6b4fad757da728"
ct = binascii.unhexlify(ct)
for i in product(x, repeat=4):
    i=''.join(i)
    j = i
    h1 = (decrypt_aes(bytes(i+y,encoding='utf8'),ct))
    set1.add(h1)
    dict1[h1] = i
    h2 = encrypt_aes(bytes(y+j,encoding='utf8'),bytes(pt,encoding='utf8'))
    set2.add(h2)
    dict2[h2] = j

k=set1.intersection(set2)
k.pop()
k=k.pop()
key1,key2=dict1[k],dict2[k]
ctt = "0f911197ffd31e81cd2235458d44904b65090bdbb4b6981807bc392cc72bb203b33906bdd1643bdb6ae554af35d8736f"
ctt = binascii.unhexlify(ctt)
ptt = decrypt_aes(bytes(key1+y,encoding='utf8'),ctt)
ptt = decrypt_aes(bytes(y+key2,encoding='utf8'),ptt)
print(ptt)
