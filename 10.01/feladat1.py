i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

for j in range(1, 11):
    print(j, end=" ")
print()



i = 1
while i <= 6:
    print(2 * i - 1, end=" ")
    i += 1
print()

for j in range(1, 12, 2):
    print(j, end=" ")
print()



a1 = 0
a2 = 1
print(a1, a2, end=" ")
i = 0
while i < 8:
    an = a1 + a2
    a1 = a2
    a2 = an
    print(an, end=" ")
    i += 1