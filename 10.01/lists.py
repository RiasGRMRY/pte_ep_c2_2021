import random

days = [31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]
months = ["jan", "feb", "márc", "ápr", "máj", "jún", "júl", "aug", "szept", "okt", "nov", "dec"]
months_and_days = []

for i in range(len(months)):
    months_and_days.append(months[i])
    months_and_days.append(days[i])
print(months_and_days)

asd = []
for i in range(20):
    asd.append(random.randint(1,100))

print(asd)
print(max(asd))
