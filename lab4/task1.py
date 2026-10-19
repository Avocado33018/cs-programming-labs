current = float(input())
target = float(input())

if current > target:
    print("Охлаждение")
elif current < target:
    print("Нагрев")
else:
    print("Выключен")
