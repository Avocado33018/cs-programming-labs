n = int(input())
odd_count = 0

for r in range(n):
    current_val = 1
    for k in range(r + 1):
        if k == 0:
            print(current_val, end="")
        else:
            print(f" {current_val}", end="")

        if current_val % 2 != 0:
            odd_count += 1

        current_val = current_val * (r - k) // (k + 1)
    print()

print(f"Нечетных элементов: {odd_count}")

