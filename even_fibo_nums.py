n = 4000000
liste = []
i = 1
j = 1
while i <2* n:
    liste.append(j)
    liste.append(i)
    j = i + j
    i = i + j
print(liste)
liste2 = []
for i in liste:
   if i % 2 == 0:
       liste2.append(i)
sum = sum(liste2) 
print(sum)