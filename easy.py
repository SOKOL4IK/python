#Задание "Easy"
# Задача - 1

a = str(print("Привет!"))
b = str(input("Введите имя: "))
print("Здравствуй " + b) 

print("Следующая задача")

# Задача - 2
UserAnswer = int(input("Введите число: "))
Answer = UserAnswer + 2
print(Answer)

print("Следующая задача")

# Задача-3
Year = int(input("Введите свой возраст: "))
if Year >= 18:
	print("Доступ разрешён")
elif Year < 18:
	print("Извините, пользование данным ресурсом только с 18 лет!")	