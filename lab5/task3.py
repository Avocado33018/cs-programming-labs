n = int(input())
count_below = 0
count_zero = 0
count_above = 0

for _ in range(n):
    temp = float(input())
    if temp < 0:
        count_below += 1
    elif temp == 0:
        count_zero += 1
    else:
        count_above += 1

print(f"Ниже нуля: {count_below}")
print(f"Равны нулю: {count_zero}")
print(f"Выше нуля: {count_above}")
