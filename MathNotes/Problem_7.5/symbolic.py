from sympy import *

x,y = symbols('x y')
z, sig = symbols('z sig')
a,b = symbols('a b')
c,d = symbols('c d')

#t = symbols('t')
#t = log(1 - x)
#print(f't is {t}')
#print(f'diff(t, x) is {latex(diff(t, x))}\n')

sig = 1 / (1 + exp(-x))
print(f'sig is {sig}')
print(f'diff(sig) is {latex(diff(sig))}\n')

a = y - 1
print(f'a is {a}')
print(f'diff(a, x) is {latex(diff(a, x))}\n')
print

b = log(1 - sig)
print(f'b is {b}')
print(f'diff(b, x) is {latex(diff(b, x))}\n')

c = y
print(f'c is {c}')
print(f'diff(c, x) is {latex(diff(c, x))}\n')

d = log(sig)
print(f'd is {d}')
print(f'diff(d, x) is {latex(diff(d, x))}\n')
