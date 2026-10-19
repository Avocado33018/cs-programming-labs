base_cost = float(input())
age = int(input())

if base_cost <= 0 or age < 0 or age > 120:
    print("Ошибка")
elif age <= 5:
    print(f"Стоимость: {0:.2f} руб")
elif age <= 17:
    print(f"Стоимость: {base_cost * 0.5:.2f} руб")
elif age <= 59:
    print(f"Стоимость: {base_cost * 1.0:.2f} руб")
else:
    print(f"Стоимость: {base_cost * 0.7:.2f} руб")
