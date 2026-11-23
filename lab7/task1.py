s = input()
if s == "":
    original = []
else:
    original = [int(x) for x in s.split()]

corrected = original.copy()

for i in range(len(corrected)):
    if corrected[i] < 0:
        corrected[i] = 0

print(f"Исходные остатки: {original}")
print(f"Исправленные остатки: {corrected}")
