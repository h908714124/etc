import sys

# Message
m = 65

# Not prime
n = 3233

# Prime
p = 3251

def inv_r(a, r):
    for i in range(0, r):
        if (i * a) % r == 1:
            return i
    raise ValueError("not invertible", a)


assert len(sys.argv) == 2, "expecting 1 argument"

a = int(sys.argv[1])

a_n = inv_r(a, n)
a_p = inv_r(a, p)

assert (a_n * a) % n == 1
assert (a_p * a) % p == 1

print "%s * %s == 1 mod %s" % (a, a_n, n)
print "%s * %s == 1 mod %s" % (a, a_p, p)

c_n = pow (m, a, n)
c_p = pow (m, a, p)

x_n = pow (c_n, a_n, n)
x_p = pow (c_p, a_p, p)

print "m = %s" % x_n
print "m = %s" % x_p 

