#Задание 4

Total_seconds = int((input()))

hours = Total_seconds // 3600
remaining_seconds = Total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
