# liste = [                      [75],
#                              [95, 64],
#                            [17, 47, 82],
#                          [18, 35, 87, 10],
#                         [20, 4, 82, 47, 65],
#                       [19, 1, 23, 75, 3, 34],
#                     [88, 2, 77, 73, 7, 63, 67],
#                   [99, 65, 4, 28, 6, 16, 70, 92],
#                 [41, 41, 26, 56, 83, 40, 80, 70, 33],
#               [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#         [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#       [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#      [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
#          ]

# i = 0
# bigger_number=0
# greatest_summation = 0
# while i <= len(liste):
#     for j in range(i,i + 2):
#         bigger_number = max(liste[i][j])
#     greatest_summation = greatest_summation + bigger_number
#     i = i + 1
# print(greatest_summation)
    

liste = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

i = 0
bigger_number = 0
greatest_summation = liste[0][0]  # İlk elemanı ekliyoruz
current_index = 0  # İlk başta seçilen sütun indeksi

while i < len(liste) - 1:
    # İki alt satırdaki uygun iki sayıdan büyüğünü seçelim
    left = liste[i + 1][current_index]  # Alt satırdaki aynı sütun
    right = liste[i + 1][current_index + 1]  # Alt satırdaki bir sağ sütun

    bigger_number = max(left, right)  # Büyük olanı seç
    greatest_summation += bigger_number  # Toplama ekle

    # En büyük sayı sağdaki ise sütun indeksini bir artır
    if bigger_number == right:
        current_index += 1
    
    i += 1

print(greatest_summation)
