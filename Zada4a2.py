#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():

    def circle():
        return math.pi * r ** 2

    r = int(input("Радиус: "))
    h = int(input("Высота: "))
    s = 2 * math.pi * r * h
    c = circle()
    p = s + 2 * c
    result = input('Вывести площадь боковой поверхности цилиндра? [y/n]: ')

    if result == 'y':
        print(f"s = {s}")
    elif result == 'n':
        print(f"c = {p}")


if __name__ == '__main__':
    cylinder()
