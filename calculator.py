import re


def valid_parentheses(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                raise SyntaxError('Кажется, Вы запутались в скобках!')
            stack.pop()
    if stack:
        raise SyntaxError('Кажется, Вы запутались в скобках!')


def parsing(formula):  # Привожу строку к валидному виду, привожу все цифры к 10ой системе

    valid_parentheses(formula) # Проверка на валидность скобок

    first_step = formula.replace('**', '^')

    if re.search(r'=\s*$', formula): # Проверка на случай, если человек решит поставить = в конце строки
        raise SyntaxError('Знак "=" не нужно ставить в конце выражения!')

    spaces = ''
    for sym in first_step:  # Так как пробелы не гарантированы, перебираю строку "вручную", чтобы отделить все символы
        if sym.isdigit() or sym in 'xo':
            spaces += sym
        elif sym == ' ':
            continue
        elif sym in '+-/*^()':
            spaces += f' {sym} '
        else:
            raise TypeError(f'Некорректный тип данных!') # Широкая проверка на валидность данных

    for obj in spaces.split(): # Проверка на валидность цифр 8 и 16 СС. Делаю ее тут, а не в начале функции, чтобы была
        # возможность вывести пользователю на экран в каком именно числе ошибка.
        if obj.startswith('0x'):
            if not re.match(r'\b0x[0-9A-F]+\b', obj):
                raise SyntaxError(f'{obj} не верно записано в шестнадцатеричной системе счисления!')
        elif obj.startswith('0o'):
            if not re.match(r'\b0o[0-7]+\b', obj):
                raise SyntaxError(f'{obj} не верно записано в восьмеричной системе счисления!!')

    # Преобразую числа и возвращаю готовый к вычислениям список
    bases = {'0x': 16, '0o': 8}
    res = [str(int(s, bases[s[:2]])) if s.startswith('0x') or s.startswith('0o') else s for s in spaces.split()]

    if re.search(r'[^0-9()][+-/*^]?[^0-9()]', ''.join(res)): # Проверка синтаксиса арифметических знаков
        raise SyntaxError('Кажется, Вы запутались в арифметических знаках!')

    return res


def shunting_yard(parsed_str):  # Алгоритм сортировочной станции. Позволяет привести список к виду ОПН.
    rpn = []
    stack = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for token in parsed_str:
        if token.isdigit():
            rpn.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack:
                x = stack.pop()
                if x == '(':
                    break
                rpn.append(x)
        elif token in '+-*/^':
            while stack and stack[-1] != '(' and priority[token] <= priority[stack[-1]]:
                rpn.append(stack.pop())
            stack.append(token)
    while stack:
        rpn.append(stack.pop())

    return rpn


def calculate(a, b, operator):  # Перевод строки-оператора в вычисления
    a, b = int(a), int(b)
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        return a / b
    elif operator == '*':
        return a * b
    elif operator == '^':
        return a ** b


def polish(rpn_str):  # Непосредственно вычисления в формате ОПН
    stack = []
    for token in rpn_str:
        if token.isdigit():
            stack.append(token)
        else:
            num2, num1 = stack.pop(), stack.pop()
            result_ = calculate(num1, num2, token)
            stack.append(result_)

    return stack[0]


def my_first_fucking_useful_calculator(user_str):
    return polish(shunting_yard(parsing(user_str)))


# Проверка
examples = {
    '10 + 0x1': 11,
    '0o10 + 10': 18,
    '0o1 + 0x1': 2,
    '(0x1 + 1) * 0x10': 32,
    '0x10 * (10 * 2 ** 3)': 1280,
    '2 * ((2 + 2) * 2 ** (1 + 0o3))': 128
}

for expr, result in examples.items():
    print(my_first_fucking_useful_calculator(expr) == result, end=' ')
print('\nУра! Всё верно!')


print('\nHello World!')  # Пользовательский ввод

while True:
    try:
        to_calculate = input('Пожалуйста, введите то, что нужно вычислить: ')
        print(f'{to_calculate} = {my_first_fucking_useful_calculator(to_calculate)}')
        next_step = input('Нужно вычислить что-то ещё? "+" если да, "-" если нет: ')
        if next_step == '-':
            break
    except (SyntaxError, TypeError) as message:
        print(message)
        print('Попробуйте ещё раз!')
    except ZeroDivisionError:
        print('На ноль нельзя делить!')
        print('Попробуйте ещё раз!')
    except Exception as message: # На всякий случай...
        print(f"Что-то пошло не так и вызвана ошибка - {message}")
        print('Попробуйте ещё раз!')

print('До свидания!')


