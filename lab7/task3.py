s = input()
if s == "":
    source = []
else:
    source = [int(x) for x in s.split()]

target = int(input())

# Используем enumerate для получения индекса и значения
indices = [i for i, val in enumerate(source) if val == target]

print(f"Индексы: {indices}")
