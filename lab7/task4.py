# Считываем размеры таблицы
r, c = map(int, input().split())

# Считываем саму таблицу как список списков
table = []
for _ in range(r):
    row = list(map(int, input().split()))
    table.append(row)

# Суммы строк
row_sums = []
for row in table:
    total = 0
    for val in row:
        total += val
    row_sums.append(total)

# Суммы столбцов
col_sums = []
for j in range(c):
    total = 0
    for i in range(r):
        total += table[i][j]
    col_sums.append(total)

print(f"Суммы строк: {row_sums}")
print(f"Суммы столбцов: {col_sums}")
