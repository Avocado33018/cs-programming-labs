s = input()
if s == "":
    source = []
else:
    source = [int(x) for x in s.split()]

squares = [x ** 2 for x in source if x > 0 and x % 2 != 0]

print(f"Квадраты: {squares}")
