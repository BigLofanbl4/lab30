# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите задачу: напишите программу, состоящую из однострочного и многострочного
#текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
#открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
#должно загружаться в поле типа Text .

import tkinter as tk


def open_file():
    file_name = entry.get()
    try:
        with open(file_name, "r", encoding="utf8") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
    except FileNotFoundError:
        text.delete("1.0", tk.END)
        text.insert(tk.END, "Файл не найден.")


def save_file():
    file_name = entry.get()
    content = text.get("1.0", tk.END)
    with open(file_name, "w") as file:
        file.write(content)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Текстовый редактор")

    entry = tk.Entry(root)
    entry.pack(pady=5)

    text = tk.Text(root, height=10, width=50)
    text.pack(pady=5)

    open_button = tk.Button(root, text="Открыть", command=open_file)
    open_button.pack(pady=5)

    save_button = tk.Button(root, text="Сохранить", command=save_file)
    save_button.pack(pady=5)

    root.mainloop()
