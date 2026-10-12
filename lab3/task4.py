s = input()
parts = s.split(";")
train_number = parts[0]
from_city = parts[1]
to_city = parts[2]
time = parts[3]
price = float(parts[4])

print(f"Поезд: {train_number}")
print(f"Маршрут: {from_city} - {to_city}")
print(f"Отправление: {time}")
print(f"Цена: {price:.2f} руб")