len_liste = []
divisors_list = []
divisors_list_len = []
tri_numbers = []

# Üçgen sayıları hesaplayan fonksiyon
def triangular_numbers(x):
    for i in range(1, x + 1):
        tri_numbers.append(int(i * (i + 1) / 2))

triangular_numbers(5000)

# Her üçgen sayının bölenlerini hesaplayan fonksiyon
def divisors(n):
    liste = []  # Her üçgen sayının bölenlerini saklamak için liste
    for j in range(1, n + 1):
        if n % j == 0:
            liste.append(j)
    return liste  # Bölenleri geri döndürüyoruz

# En uzun bölen listesi olan üçgen sayıyı bulan ve çıktıyı yazdıran kısım
def find_longest_divisors():
    max_len = 0
    number_with_max_len = 0
    divisors_with_max_len = []

    for tri_num in tri_numbers:
        div_list = divisors(tri_num)
        div_len = len(div_list)
        divisors_list.append((tri_num, div_list))
        divisors_list_len.append(div_len)
        
        # En uzun bölen listesi kontrolü
        if div_len > max_len:
            max_len = div_len
            number_with_max_len = tri_num
            divisors_with_max_len = div_list

        # Sayı ve bölenler listesini alt alta yazdırma
        print(f"{tri_num}: {div_list}")

    print(f"\nNumber with the longest divisors list: {number_with_max_len}")
    print(f"Divisors: {divisors_with_max_len}")
    print(f"Length of divisors list: {max_len}")

# Üçgen sayılarının bölenlerini hesaplayıp yazdır
find_longest_divisors()
