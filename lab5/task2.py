a = int(input())
b = int(input())

total_sum = 0
total_mult = 1

for i in range(a, b + 1):
    total_sum += i
    total_mult *= i

print(f"Сумма: {total_sum}")
print(f"Произведение: {total_mult}")
