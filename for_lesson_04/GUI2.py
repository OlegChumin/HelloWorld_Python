# Теперь добавим кнопку, которая будет менять текст при нажатии:

import tkinter as tk

def change_text():
    label.config(text="Привет, Мир!")

# Создание главного окна
root = tk.Tk()

# Установка заголовка окна
root.title("Текст в окне")

# Установка размеров окна
root.geometry("300x200")

# Создание текстовой метки
label = tk.Label(root, text="Hello, World!", font=("Arial", 20))
label.pack(pady=20)

# Создание кнопки
button = tk.Button(root, text="Нажми меня", command=change_text)
button.pack(pady=10)

# Запуск главного цикла окна
root.mainloop()
