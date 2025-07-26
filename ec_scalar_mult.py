from ecdsa.ellipticcurve import Point, CurveFp
from ecdsa.curves import SECP256k1

curve = SECP256k1.curve

x = 55066263022277343669578718895168534326250603453777594175500187360389116729240
y = 32670510020758816978083085130507043184471273380659243275938904335757337482424
scalar = 2

P = Point(curve, x, y)
Q = scalar * P

print("Result of scalar multiplication:")
print(f"Q.x = {Q.x()}")
print(f"Q.y = {Q.y()}")

