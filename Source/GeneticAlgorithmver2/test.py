import numpy as np
"""
x = np.arange(10)
print(x)

for i in range(10):
    x = np.random.choice(np.arange(5), p = np.array([0.5, 0.4, 0.05, 0.025, 0.025]))
    print(x)

a = np.arange(8)
b = np.array([99,88,77,66,55,44,33,22])
def mix(a, b):
    return np.append(a[4:], b[:4])

def mutate(a):
    for i in range(len(a)):
        if np.random.choice([0,1], p = [0.95, 0.05]) == 1:
            a[i] = np.random.randint(8)
print(mix(a,b))

for i in range(100):
    mutate(a)
print(a)"""

a = np.zeros((5,5))
print(a)
b = np.arange(5)
print(b)
a[0] = np.copy(b)
print(a)
a[1] = np.copy(b)
print(a)