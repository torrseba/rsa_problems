from Crypto.Util.number import *
msg=b"UDCTF{0k_m4yb3_d0nt_u5e_e_3qu4l5_3}"
pt=bytes_to_long(msg)
p=getPrime(1024)
q=getPrime(1024)
N=p*q
e=3
ct=pow(pt,e,N)

print(N)
print(e)
print(ct)
