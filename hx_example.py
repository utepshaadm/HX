# HX Example
from heka import HEKA
from hx import HX
from random import shuffle

# Encryption
msg ="ATTACKATDAWN"
nonce = list(range(52))
shuffle(nonce)
heka = HEKA()
heka.gen_rand_decks()
heka.add_nonce(nonce)
key = list(heka.deck)
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

keyhx = HX()
keyhx.deck = list(key)
key2 = keyhx.mac("A")

hxd = HX()
tmp = hxd.mac(key2)
verify = hxd.mac(ctxt)
print(verify)

hekad = HEKA()
hekad.add_nonce(nonce)
hekad.deck = list(key)
ptxt = hekad.decrypt(ctxt)
print(ptxt)
