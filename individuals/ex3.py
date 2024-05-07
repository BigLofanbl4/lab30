# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите задачу: перепишите программу из пункта 8 так, чтобы интерфейс выглядел
#примерно следующим образом:

import tkinter as tk


def set_color(hex_color):
    color_name_label.config(text=rainbow_colors[hex_color])
    color_code_entry.delete(0, tk.END)
    color_code_entry.insert(0, hex_color)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Цвета радуги")

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(side=tk.BOTTOM, padx=2, pady=2)

    rainbow_colors = {
        "#ff0000": "Красный",
        "#ff7d00": "Оранжевый",
        "#ffff00": "Желтый",
        "#00ff00": "Зеленый",
        "#007dff": "Голубой",
        "#0000ff": "Синий",
        "#7d00ff": "Фиолетовый",
    }

    for hex_color in rainbow_colors:
        button = tk.Button(
            buttons_frame,
            bg=hex_color,
            width=2,
            command=lambda c=hex_color: set_color(c),
        )
        button.pack(side=tk.LEFT, padx=1, pady=1)

    color_code_entry = tk.Entry(root, justify="center")
    color_code_entry.pack()

    color_name_label = tk.Label(root, text="")
    color_name_label.pack()

    root.mainloop()
