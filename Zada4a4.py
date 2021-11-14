#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    return input('Запрос ввода: ')


def test_input(a):
    if type(a) == int or type(a) == float:
        return True
    elif a.isnumeric():
        return True
    else:
        return False


def str_to_int(b):
    return int(b)


def print_int(c):
    print(c)


d = get_input()
if test_input(d):
    print_int(str_to_int(d))


if __name__ == '__main__':
    get_input()
