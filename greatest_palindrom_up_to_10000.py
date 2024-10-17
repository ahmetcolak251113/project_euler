
liste = []
liste1 = []
for i in range(100,1000):
    for j in range(100,1000):
        liste.append(i*j)

for m in liste:
    m1 = str(m)
    if m1 == m1[::-1]:
        liste1.append(m)
print(max(liste1))