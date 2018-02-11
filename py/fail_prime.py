# Prime
n = 3251

# The public key
e = 65

# Clear message
m = 23

# Encrypted message
c = 1862

def exp(a, b):
    """
    Exponentiation mod n
    """
    return pow(a, b, n)

def times(a, b):
    """
    Multiplication mod n
    """
    return (a * b) % n

# Checking that c is really the encrypted message
assert c == exp (m, e)

# Let's guess the private key
e_ = 3201

# e_ is the multiplicative inverse of the pubkey e.
# It can be found efficiently, using the extended euclidean algorithm.
assert times (e_, e) == 1

# Will it work?
assert exp (c, e_) == m, "exp (c, e_) is not %r but %r" % (m, exp (c, e_))

