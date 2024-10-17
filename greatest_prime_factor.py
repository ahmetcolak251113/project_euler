# Prime factor
import math
liste = []
liste2 = []
def prime_factor(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            liste.append(i)
    #print(liste)
    for j in liste:
        for i in liste:
            if j > i and j % i == 0:
                liste2.append(i)
            else:
                continue
    #print(set(liste2))
    liste3 = list(set(liste2))
    #print(liste3)
    maxpf = max(liste3)
    print(maxpf)
prime_factor(600851475143)