from sympy import *
from Crypto.Util.number import *
import random
p=getPrime(512)
q = nextprime(p + random.randint(10**9,10**10))
N=p*q
msg=b'UDCTF{4n_RSA_5ch0ol_gr4dua73!!}'
pt = bytes_to_long(msg)
e = 65537
ct = pow(pt, e, N)
print(N)
print(e)
print(ct)
