# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def set_color(hex_color):
    color_code_entry.delete(0, tk.END)
    color_code_entry.insert(0, hex_color)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Цвета радуги")

    color_code_entry = tk.Entry(root, justify="center")
    color_code_entry.pack()

    rainbow_colors = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff7d00",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#007dff",
        "Синий": "#0000ff",
        "Фиолетовый": "#7d00ff",
    }

    for color_name, hex_color in rainbow_colors.items():
        button = tk.Button(
            root, bg=hex_color, command=lambda h=hex_color: set_color(h)
        )
        button.pack(fill=tk.X)

    root.mainloop()
