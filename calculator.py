def parsing(formula):  # Привожу строку к валидному виду, привожу все цифры к 10ой системе
    bases = {'0x': 16, '0o': 8}

    first_step = formula.replace('**', '^')
    spaces = ''
    for sym in first_step:  # Так как пробелы не гарантированы, перебираю строку "вручную", чтобы отделить все символы
        if sym.isdigit() or sym in 'xo':
            spaces += sym
        elif sym == ' ':
            continue
        elif sym in '+-/*^()':
            spaces += f' {sym} '
        else:
            pass  # Оставила место для ошибки - если некорректный символы в строке. Или это не так делается?

    res = [str(int(s, bases[s[:2]])) if s.startswith('0x') or s.startswith('0o') else s for s in spaces.split()]
    # Преобразую числа и возвращаю готовую к вычислениям строку
    # Нужно ли делать проверку корректности формата числе 8 и 16 СС ?

    return res


def shunting_yard(parsed_str):  # Алгоритм сортировочной станции. Позволяет привести строку к виду ОПН.
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


def polish(rpn_str):  # Непосредственно вычисления в формате ОПН.

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

    stack = []
    for token in rpn_str:
        if token.isdigit():
            stack.append(token)
        else:
            num2, num1 = stack.pop(), stack.pop()
            result = calculate(num1, num2, token)
            stack.append(result)

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
    to_calculate = input('Пожалуйста, введите то, что нужно вычислить: ')
    print(f'{to_calculate} = {my_first_fucking_useful_calculator(to_calculate)}')
    next_step = input('Нужно вычислить что-то ещё? "+" если да, "-" если нет: ')
    if next_step == '-':
        break
print('До свидания!')







