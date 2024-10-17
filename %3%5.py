liste = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        liste.append(i)
sum = sum(liste)

print(liste)
print(sum)