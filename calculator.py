import math
d = str()
a = float()
while d == "":
    c = input("Select operation (+,-,*,/,^,sqrt,fact,sin,cos,tan,exit)")
    if c == "+" or c == "-" or c == "*" or c == "/" or c == "^" or c == "sqrt" or c == "fact" or c == "sin" or c == "cos" or c == "tan" or c == "exit": 
        if c == 'exit':
                exit()
        if c == 'sqrt':
                if a is not float:
                        try:
                                a = float(input())
                                if a < 0:
                                        print('нет отрицательного корня ')
                                else:
                                        print(math.sqrt(a))
                        except ValueError:
                                print("не число")
                continue
        elif c == 'fact':
                if a is not int:
                        try:
                                a = int(input())
                                if a == 0 or a < 0:
                                        print('нет факториала 0 и отрицательного числа')
                                else: 
                                        print(math.factorial(a))
                        except ValueError:
                                print("не число")
        elif c == 'sin':
                if a is not float:
                        try:
                                a = float(input())
                        except ValueError:
                                print("не число")
                        else:
                                print(math.sin(a))
        elif c == 'cos':
                if a is not float:
                        try:
                                a = float(input())
                        except ValueError:
                                print("не число")
                        else:
                                print(math.cos(a))
        elif c == 'tan':
                if a is not float:
                        try:
                                a = float(input())
                        except ValueError:
                                print("не число")
                        else:
                                print(math.tan(a))
        else:
                if c == '+': 
                        if a is not float or b is not float:
                                try:
                                        a = float(input())
                                        b = float(input())
                                except ValueError:
                                        print("не число")
                                else:
                                        print(a+b)
                elif c == '-':
                        if a is not float or b is not float:
                                try:
                                        a = float(input())
                                        b = float(input())
                                except ValueError:
                                        print("не число")
                                else:
                                        print(a-b)
                elif c == '*':
                        if a is not float or b is not float:
                                try:
                                        a = float(input())
                                        b = float(input())
                                except ValueError:
                                        print("не число")
                                else:
                                        print(a*b)
                elif c == '/':
                        if a is not float or b is not float:
                                try:
                                        a = float(input())
                                except ValueError:
                                        print("не число")
                                        continue
                                try:
                                        b = float(input())
                                        if b == 0:
                                                print('на 0 делить нельзя')
                                        else:
                                                print(a/b)
                                except ValueError:
                                        print("не число")
                elif c == '^':
                        if a is not int or b is not int:
                                try:
                                        a = int(input())
                                        b = int(input())
                                except ValueError:
                                        print("не число")
                                else:
                                        print(a**b)
    else:
            print("неверный оператор")