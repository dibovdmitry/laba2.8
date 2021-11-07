#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder(r, h):
    from math import pi


    def circle():
        s = 2*pi*r*h
        if input('Full area? [y/n]: ') == 'y': \
            s += 2*circle(r)
        return circle()


       print('s =', cylinder(r, h))