#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    answer = 1
    while 1:
        num = int(input())
        if not num:
            break
        answer *= num
    return answer


print(test())

if __name__ == '__main__':
    test()
