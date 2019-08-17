#Задание "Normal"
#Задача 1
UserAnswer = int(input("Введите число от 0 до 10: "))

while UserAnswer >= 10 :
	UserAnswer = int(input("Попробуйте снова: "))
	
a = UserAnswer ** 2	
print(a)

#Задача 2
UserAnswer_1 = input("Введите первое число: ")
UserAnswer_2 = input("Введите второе число: ")
print("Ваши числа " + UserAnswer_2 + " " + UserAnswer_1)