# Дано целое число N (> 0). Найти сумму 1^N + 2^N + ... + .. ^N.
N = int(input("Введите целое число N (> 0): "))
try:
    total_sum = 0
    for i in range( 1, N+1 ):
        total_sum += i ** N
    print("Сумма:", total_sum)
except :
    print("Что то пошло не так ((")