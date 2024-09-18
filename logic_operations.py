x = 5
y = 10

#   True  and  True == True
if x > 0 and y > 5:
    print(" Оба условия истинны")
else:
    print("Одно или более условий ложный")

a = -5
b = 10

#  False or True == True
if a > 0 or b > 5:
    print("Одно из условий истинно")
else:
    print("Оба условия ложны")


с = 5

if not с < 0:
    print(" Число положительное ")
else:
    print("Число отрицательное")

z = 15
#   True   and   (True  or  False == True)
if x > 0 and (y == 10 or z == 20):
    print("Условие выполнено")
else:
    print("Условие не выполнено")


a = True
b = False
#       True   False
result = a and b
print(result)

result = a or b
print(result)

result = not a
print(result)

age = 17
if age >= 18 and age < 60:
    print("Взрослый")
else:
    print("Молодой или пенсионер")
            #       0         1          2
shopping_list = ["apples", "bananas", "bread"]
if "apples" in shopping_list and "milk" not in shopping_list:
    print("Яблоки есть, но молока нет в списке покупок")

empty_list = []

fruits = ["apple", "banana", "cherry"]

first_fruit = fruits[0]
print(first_fruit)

last_fruit = fruits[-1]
print(last_fruit)

fruits.append("oranges")
print(fruits)

fruits.insert(1, "blueberry")
print(fruits)

del fruits[0]
print(fruits)

removed_first = fruits.pop(0)
print(removed_first)
print(fruits)

sublist = fruits[1:]
print(sublist)
sublist2 = fruits[:2]
print(sublist2)

fruits.append("oranges")
fruits.append("oranges")
print(fruits)

sublist3 = fruits[1:4]
print(sublist3)

