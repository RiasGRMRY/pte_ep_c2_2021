sz1 = "alma"

if sz1[0] == sz1[-1]:
    print("Megegyezik ")
else:
    print("Nem egyezik")

n1 = 0

if n1 >= 0:
    print("Pozitiv")
else:
    print("negativ")

if sz1[0].isupper():
    print("Nagybetüvel kezdödik")
else:
    print("Nem nagybetüvel kezdödik")

n2 = 10
n3 = 100

if n2 % n3 == 0:
    print(n3, "Osztoja", n2, "-nak")
else:
    if n3 % n2 == 0:
        print(n2, "Osztoja", n3, "-nek")
    else:
        print("Egyik sem osztoja a masiknak")

sz2 = "asda."
print(sz2[-1])

a, b, c = 4, 5, 7

if a > b and a > c:
    print(a, "A legnagyobb szam")
elif b > a and b > c:
    print(b, "A legnagyobb szam")
else:
    print(c, " A legnagyobb szam")

if a < b and a < c:
    print(a, "A legkisebb szam")
elif b < a and b < c:
    print(b, "A legkisebb szam")
else:
    print(c, " A legkisebb szam")

char = "a"
print(char.isascii())

