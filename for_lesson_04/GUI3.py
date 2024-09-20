# Вывод текста по нажатию клавиши:
# Теперь добавим возможность выводить текст по нажатию клавиши:

import tkinter as tk

def on_key(event):
    label.config(text=f"Вы нажали: {event.char}")

# Создание главного окна
root = tk.Tk()

# Установка заголовка окна
root.title("Нажмите клавишу")

# Установка размеров окна
root.geometry("300x200")

# Создание текстовой метки
label = tk.Label(root, text="Нажмите любую клавишу", font=("Arial", 20))
label.pack(pady=50)

# Привязка события нажатия клавиши
root.bind('<Key>', on_key)

# Запуск главного цикла окна
root.mainloop()
