from math import lcm, modf
import binascii

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


p = 1000
q = p * 10 - 1

while not is_prime(p):
    p+=1

while not is_prime(q):
    q-=1

n = q * p

lmbda = lcm(p-1, q-1)
e = 31 
d = pow(e, -1, lmbda)

print(f"Arda's public key: ({n}, {e})")
msg ="hi"
msg_int = int(binascii.hexlify(msg.encode("utf-8")),16)
print(msg_int)

encrypted = msg_int**e % n
print(encrypted)
decrypted = encrypted**d % n
print(decrypted)
print(binascii.unhexlify(hex(decrypted)[2:].encode('ascii')).decode('utf-8'))