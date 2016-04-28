# -*- coding: utf-8 -*-
# !/usr/bin/env python

import cgi


print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head><title>Разложение числа на множители</title></head>")
print("<body>")
print('<form method="post" action="factor.py">')
print('</form>')
form = cgi.FieldStorage()                  # передаем переменную в форму
if form.getvalue("number"):
    number = int(form.getvalue("number"))  # введенное значение в форму - число

    def factor(number):                    # разложение числа на множители
        a = []
        d = 2
        while d * d <= number:             # проверяем делимость number на
            if number % d == 0:            # натуральные числа, начиная с 2
                a.append(d)                # добавляем делитель в список
                number //= d
            else:
                d += 1
        if number > 1:                     # продолжаем перебор пока number не будет равно 1
            a.append(number)               # добавляем number к списку простых делителей
        return str(a)                      # возвращается строка

    print('<h2>' + factor(number) + '<h2><br />')  # вывод результата расчета функции
print("</body>")
print("</html>")

