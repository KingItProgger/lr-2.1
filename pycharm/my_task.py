#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    a = float(input("Введите длину параллелепипеда: "))
    b = float(input("Введите ширину параллелепипеда: "))
    c = float(input("Введите высоту параллелепипеда: "))
    v = a * b * c
    s = 2 * (a * b + b * c + a * c)
    print("Объем параллелепипеда:", v)
    print("Площадь боковой поверхности:", s)