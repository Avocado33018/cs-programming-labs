s = input()
length = len(s)
is_alpha = s.isalpha()
is_digit = s.isdigit()
is_alnum = s.isalnum()
has_dash = "-" in s

print(f"Длина: {length}")
print(f"Только буквы: {is_alpha}")
print(f"Только цифры: {is_digit}")
print(f"Буквенно-цифровая: {is_alnum}")
print(f"Содержит дефис: {has_dash}")