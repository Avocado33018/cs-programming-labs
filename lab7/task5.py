r, c = map(int, input().split())

table = []
for _ in range(r):
    row = list(map(int, input().split()))
    table.append(row)

r_start, r_end, c_start, c_end = map(int, input().split())
target = int(input())

found = False
for i in range(r_start, r_end + 1):
    for j in range(c_start, c_end + 1):
        if table[i][j] == target:
            print(i, j)
            found = True

if not found:
    print("Не найдено")
