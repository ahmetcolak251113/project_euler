n = 100
summ = n*(n + 1) / 2
liste = []
for i in range(n+1):
    liste.append(i)
print(liste)
sqrsum = sum(x**2 for x in liste)
print(summ) 
print(sqrsum)
print(abs(sqrsum-summ**2))