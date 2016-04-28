# -*- coding: utf-8 -*-
# !/usr/bin/env python


import unittest


def factor(number):
    a = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            a.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        a.append(number)
    return str(a)


class Test(unittest.TestCase):

    def test_negativenumber(self):
        for number in range(0, -42):
            self.assertFalse(factor(number))

    def test_normnumber(self):
        self.assertTrue(factor(42))

if __name__ == '__main__':
    unittest.main()