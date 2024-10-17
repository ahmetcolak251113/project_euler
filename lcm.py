

import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

# Örnek bir liste
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Listedeki sayıların en küçük ortak katını bulma
result = lcm_of_list(numbers)

print(result)

lcm_of_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])