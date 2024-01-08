#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    hours = int(input("Введите часы: "))
    minutes = int(input("Введите минуты: "))
    seconds = int(input("Введите секунды: "))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    angle = (total_seconds / 86400) * 360
    print(angle)
