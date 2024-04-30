# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def select():
    label.config(text=var.get())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Radiobutton с indicatoron=0")

    frame_radio_buttons = tk.Frame(root)
    frame_radio_buttons.pack(side=tk.LEFT, fill=tk.Y, expand=False)

    frame_output = tk.Frame(root)
    frame_output.pack(side=tk.RIGHT, fill=tk.X, anchor="center", expand=True)

    var = tk.StringVar(value="Выберите опцию")

    label = tk.Label(frame_output, text=var.get(), justify="center")
    label.pack(padx=10)

    radiobuttons = [
        ("Опция 1", "Опция 1"),
        ("Опция 2", "Опция 2"),
        ("Опция 3", "Опция 3"),
    ]

    for text, value in radiobuttons:
        rb = tk.Radiobutton(
            frame_radio_buttons,
            text=text,
            variable=var,
            value=value,
            indicatoron=0,
            command=select,
            width=20,
            height=2,
        )
        rb.pack()

    root.mainloop()
