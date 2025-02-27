# EC operations

This repository contains implementations of elliptic curve operations over a finite field as part of the Security Protocols course at Tampere University.

Implemented Functions:
addEC(x, y, c) – Adds two points on the elliptic curve:
y^2 = x^3 + a * x + b mod p
doubleEC(x, c) – Computes the doubling of a point on the curve using:
lambda = (3 * x1^2 + a) / (2 * y1) mod p
x3 = lambda^2 - 2 * x1 mod p
y3 = lambda * (x1 - x3) - y1 mod p
Key Features:
Modular arithmetic operations over prime fields.
Handles the point at infinity, represented as [0, 0].
Assumes the given points lie on a valid elliptic curve.
These functions form the basis for elliptic curve cryptographic operations and will be extended in future tasks.