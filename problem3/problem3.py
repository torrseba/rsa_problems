from Crypto.Util.number import *
p=getPrime(512)
q=getPrime(512)
n=p*q
e1=71
e2=101
msg=bytes_to_long(b'UDCTF{3uc1id_th4_60at}')
c1 = pow(msg, e1, n)
c2 = pow(msg, e2, n)
print(n)
print(e1)
print(e2)
print(c1)
print(c2)
