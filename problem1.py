def problem1():
    from Crypto.Util.number import *
    p=getPrime(512)
    q=getPrime(512)
    n=p*q
    e=65537
    msg=bytes_to_long(b'UDCTF{y3a_b0i_b4by_RSA!}')
    ct=pow(msg,e,n)
    print(p)
    print(n)
    print(e)
    print(ct)

def problem2():
    from Crypto.Util.number import *
    n=166045890368446099470756111654736772731460671003059151938763854196360081247044441029824134260263654537
    e=65537
    msg=bytes_to_long(b'UDCTF{pr1m3_f4ct0r_the1f!}')
    ct=pow(msg,e,n)
    print(n)
    print(e)
    print(ct)
    
def problem3():
    from Crypto.Util.number import *
    p=getPrime(512)
    q=getPrime(512)
    n=p*q
    e1=71
    e2=101
    msg=bytes_to_long("UDCTF{3uc1id_th4_60at}")
    c1 = pow(msg, e1, n)
    c2 = pow(msg, e2, n)
    print(n)
    print(e1)
    print(e2)
    print(c1)
    print(c2)

def problem5():
    from Crypto.Util.number import *
    e=65537
    your_e = getPrime(20)
    msg=bytes_to_long("ninja{REDACTED}")
    p=getPrime(512)
    q=getPrime(512)
    n=p*q
    assert(msg < n)
    ct=pow(msg, e, n)
    your_d = inverse(your_e, (p-1)*(q-1))
    print(your_e)
    print(your_d)
    print(n)
    print(e)
    print(ct)
