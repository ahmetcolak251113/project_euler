len_liste = []
divisors_list = []
divisors_list_len = []
tri_numbers = []
def triangular_numbers(x):
    for i in range(1, x + 1):
        tri_numbers.append(int(i * (i + 1) / 2))
triangular_numbers(10000)
def divisors(n):
    liste = []
    for j in range(1, n + 1):
        if n % j == 0:
            liste.append(j)
    return liste
def find_longest_divisors():
    max_len = 0
    number_with_max_len = 0
    divisors_with_max_len = []
    for tri_num in tri_numbers:
        div_list = divisors(tri_num)
        div_len = len(div_list)
        divisors_list.append((tri_num, div_list))
        divisors_list_len.append(div_len)
        if div_len > max_len:
            max_len = div_len
            number_with_max_len = tri_num
            divisors_with_max_len = div_list
            
        print(f"{tri_num}: {div_list}")
    print(f"\nNumber with the longest divisors list: {number_with_max_len}")
    print(f"Divisors: {divisors_with_max_len}")
    print(f"Length of divisors list: {max_len}")
    if div_len == 500:
        print(f"{tri_num}: {div_list}")
    print(f"\nNumber with the longest divisors list: {number_with_max_len}")
    print(f"Divisors: {divisors_with_max_len}")
    print(f"Length of divisors list: {max_len}")
    print(f"Max len of divisors list number: {tri_num}")
find_longest_divisors()
