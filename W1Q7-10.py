import numpy as np


# =====================================================
# Question 7
# (1 + x^3)y' + 3x^2 y = cos(x), y(0) = 1
# =====================================================

def y_q7(x):
    return (1 + np.sin(x)) / (1 + x**3)


x7 = np.array([0.0, 0.5, 1.0])

print("Question 7:")
print(y_q7(x7))


# =====================================================
# Question 8
# y' + lambda*y = exp(-lambda*x), y(0) = 1
# =====================================================

def y_q8(x, lam):
    return (1 + x) * np.exp(-lam * x)


lam = 2.0
x8 = np.array([0.0, 0.5, 1.0])

print("\nQuestion 8:")
print(y_q8(x8, lam))


# =====================================================
# Question 9
# Mortgage
# =====================================================

monthly_payment = 1200
annual_payment = monthly_payment * 12

r = 0.05
T = 30

B0 = (annual_payment / r) * (1 - np.exp(-r * T))

print("\nQuestion 9:")
print("Maximum mortgage =", B0)
print("Closest answer = $224,000")


# =====================================================
# Question 10
# Escape velocity
# =====================================================

g = 9.81
R = 6.371e6

v_escape = np.sqrt(2 * g * R)

print("\nQuestion 10:")
print("Escape velocity =", v_escape, "m/s")
print("Escape velocity =", v_escape / 1000, "km/s")
