s = input()
category = s[:3]
year = s[4:8]
number = s[9:13]
reverse_number = number[::-1]

print(f"Категория: {category}")
print(f"Год: {year}")
print(f"Номер: {number}")
print(f"Обратный номер: {reverse_number}")