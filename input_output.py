import os
# from pathlib import Path

with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

poem = """Скажи-ка, дядя, ведь недаром
Москва, спалённая пожаром,
Французу отдана?
Ведь были ж схватки боевые,
Да, говорят, ещё какие!
Недаром помнит вся Россия
Про день Бородина!"""

with open('borodino.txt', 'w', encoding='utf-8') as file:
    file.write(poem)

with open('borodino.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

directory = 'C:\\Users\\tschu\\PycharmProjects\\HelloWorld'

for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        print(file)

# path = Path(directory)
# for item in directory.iterdir():
#     if item.is_file():
#         print(item)



with open('borodino.txt', 'a', encoding='utf-8') as file:
    file.write('\nНовая строка, добавленная в конец файла')

with open('borodino.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
