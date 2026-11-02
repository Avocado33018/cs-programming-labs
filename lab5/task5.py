total_cost = 0
count = 0

while True:
    s = input()
    if s == "stop":
        break

    cost = int(s)
    total_cost += cost
    count += 1

if count == 0:
    print("Нет покупок")
else:
    avg = total_cost / count
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total_cost} руб")
    print(f"Средняя стоимость: {avg:.2f} руб")
