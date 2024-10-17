
def collatz_sequence_length(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count + 1  # Başlangıç sayısını da sayıyoruz

def longest_collatz_sequence(limit):
    longest_length = 0
    number_with_longest = 0
    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > longest_length:
            longest_length = length
            number_with_longest = i
    return number_with_longest, longest_length

limit = 1000000
result = longest_collatz_sequence(limit)
print(f"The number with the longest Collatz sequence is {result[0]} with a length of {result[1]}.")
