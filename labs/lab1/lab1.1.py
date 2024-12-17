def is_abundant(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) > n

n = int(input("Введіть ціле число n: "))

if is_abundant(n):
    print(f"Число {n} є надлишковим.")
else:
    print(f"Число {n} не є надлишковим.")
