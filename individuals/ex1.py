# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите задачу: напишите простейший калькулятор, состоящий из двух текстовых полей,
#куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат вычисления
#должен отображаться в метке. Если арифметическое действие выполнить невозможно
#(например, если были введены буквы, а не числа), то в метке должно появляться слово
#"ошибка".

import tkinter as tk


def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        match operation:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                result = num1 / num2
        label_result.config(text=f"Результат: {result}")
    except (ValueError, ZeroDivisionError):
        label_result.config(text="Ошибка")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор")

    entry_num1 = tk.Entry(root)
    entry_num2 = tk.Entry(root)
    entry_num1.pack()
    entry_num2.pack()

    btn_add = tk.Button(root, text="+", command=lambda: calculate("+"))
    btn_sub = tk.Button(root, text="-", command=lambda: calculate("-"))
    btn_mul = tk.Button(root, text="*", command=lambda: calculate("*"))
    btn_div = tk.Button(root, text="/", command=lambda: calculate("/"))
    btn_add.pack()
    btn_sub.pack()
    btn_mul.pack()
    btn_div.pack()

    label_result = tk.Label(root, text="Результат: ")
    label_result.pack()

    root.mainloop()
