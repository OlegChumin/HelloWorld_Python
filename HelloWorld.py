print('Hello World')

print("Hello World")

# Ввод строки
name = input("Введите ваше имя: ")

# Ввод целого числа
age = int(input("Введите ваш возраст: "))

# Ввод числ с плавающей точкой
height =  float(input("Введите ваш рост в м (например 1.75): "))

print(f"Привет, {name}! Вам {age} лет и ваш рост составляет {height: .2f} метра.")

for i in range(5):
    print(i)

fruits = ["apple", "banana", "orange", "cherry"]
for i in fruits:
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1 # i = 1 + 1

x  = 7

if x > 10:
    print("x больше 10")
elif x == 7: #else if
    print("x равно 7")
else:
    print("x меньше 10")
