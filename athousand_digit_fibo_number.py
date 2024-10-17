
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# liste = []
# n = 50
# for i in range(1,n):
#     liste.append(fibonacci_recursive(i))

# liste1 = []    
# for i in liste:
#     if len(str(i))==1000:
#         liste1.append(i)

def find_first_fib_with_digits(digit_count):
    a, b = 1, 1
    index = 2  # İlk iki Fibonacci sayısı zaten biliniyor (1, 1)
    
    while len(str(b)) < digit_count:
        a, b = b, a + b
        index += 1

    return index, b

# İlk 1000 basamaklı Fibonacci sayısını bul
index, fib_number = find_first_fib_with_digits(10)
print(f"İlk 1000 basamaklı Fibonacci sayısı, Fibonacci dizisindeki {index}. terimdir.")
