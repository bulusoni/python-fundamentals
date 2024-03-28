####### Bitwise Operators &, |, ^, ~ #######

a = 4
b = 3
print(a & b)
print(a | b)
print(a ^ b)

# NOT (2's complement: Convert to binary + 1)
print(~a)
print(~b) 

# LEFT Shift Operator
a = 5
print(a<<2)

# RIGHT Shift Operator
a = 5
print(a>>2)

# Lonely Integer

xor=0
a = [1, 3, 4, 3, 2, 1]
for i in range(len(a)):
    xor = xor^a[i]
print(xor)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p[0] = a[i]
for i in range(len(a)):
    if i==0:
        continue
    p[i]=p[i-1]^a[i]
print(p)
