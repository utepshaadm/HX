# HX Example
from heka import HEKA
from hx import HX
from random import shuffle
from hx_kdf import HXKDF

# Encryption
msg ="ATTACKATDAWN"
phrase = "SECRET"
kdf = HXKDF()
key = kdf.kdf(phrase)
nonce = list(range(52))
shuffle(nonce)
heka = HEKA(key)
heka.add_nonce(nonce)
keyhx = HX()
keyhx.deck = list(key)
key2 = keyhx.mac("A")
ctxt = heka.encrypt(msg)
print(ctxt)
hx = HX()
tmp = hx.mac(key2)
tag = hx.mac(ctxt)
print(tag)

# Decryption
kdf = HXKDF()
key = kdf.kdf(phrase)

keyhx = HX()
keyhx.deck = list(key)
key2 = keyhx.mac("A")

hxd = HX()
tmp = hxd.mac(key2)
verify = hxd.mac(ctxt)
print(verify)

hekad = HEKA(key)
hekad.add_nonce(nonce)
ptxt = hekad.decrypt(ctxt)
print(ptxt)
