# Дано целое число N (> 0). Найти сумму 1^N + 2^N-1 + ... + N^1.
N = int(input("Введите целое число N (> 0): "))
total_sum = 0
for i in range(1, N + 1):
    total_sum += i ** (N - i + 1)
print("Сумма:", total_sum)