#044

a = 0b11101100
b = 0b10111011

print(bin(a & b), a & b)
print(bin(a ^ b), a ^ b)
print(bin(a | b), a | b)
print(bin((a + b) >> 2), (a + b) >> 2)
print(bin(~a), ~a)
