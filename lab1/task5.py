#Задание 5
distance = float(input())
fuel_consumption_per_100km = float(input())
fuel_price_per_liter = float(input())

fuel_needed = (distance / 100) * fuel_consumption_per_100km
total_cost = fuel_needed *  fuel_price_per_liter

print(f"Топливо: {total_cost:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб")