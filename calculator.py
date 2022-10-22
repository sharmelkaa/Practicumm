# easy = '10+ 0x1**2'
# easy = '2 * ((2 + 2) * 2 ** (1 + 0o3))'
easy = '2 + 10**2 - 5 * 3**4'
num = ''

def calculate(a, b, operation): # перевод строки-оператора в вычисления
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/':
        result = a / b
    elif operation == '*':
        result = a * b
    elif operation == '**':
        result = a ** b
    return result


for index in range(0, len(easy)):  # преобразую исходную строку в список символов
    if easy[index].isdigit() or easy[index] in 'xo':
        num += easy[index]
    elif easy[index] == ' ':
        continue
    elif easy[index] == '*':
        if easy[index+1] == '*':
            num += f' ** '
        elif easy[index+1] != '*' and easy[index-1] != '*':
            num += f' {easy[index]} '
    else:
        num += f' {easy[index]} '
print(num.split())
splited = num.split()


for sym in range(0, len(splited)): # преобразую числа в 10ную систему все
    if splited[sym].isdigit():
        splited[sym] = int(splited[sym])
    elif splited[sym].startswith('0x'):
        splited[sym] = int(splited[sym], 16)
    elif splited[sym].startswith('0o'):
        splited[sym] = int(splited[sym], 8)
print(splited)


priority = {'**': 1, '*': 2, '/': 2, '+': 3, '-': 3}
flag = True
while flag == True: # сначала вычисляю все возведения в степень
    for indx in range(0, len(splited)):
        if splited[indx] == '**':
            new_num = calculate(splited[indx - 1], splited[indx + 1], splited[indx])
            splited[indx - 1] = new_num
            del splited[indx:indx + 2]
            if '**' not in splited:
                flag = False
                break
print(splited)
flag = True
while flag == True: # затем вычисляю деление и умножение
    for indx in range(0, len(splited)):
        if splited[indx] == '/':
            new_num = calculate(splited[indx - 1], splited[indx + 1], splited[indx])
            splited[indx - 1] = new_num
            del splited[indx:indx + 2]
        elif splited[indx] == '*':
            new_num = calculate(splited[indx - 1], splited[indx + 1], splited[indx])
            splited[indx - 1] = new_num
            del splited[indx:indx + 2]
        if '*' not in splited and '/' not in splited:
            flag = False
            break
print(splited)

flag = True
while flag == True:  # затем вычисляю сложение и вычитание
    for indx in range(0, len(splited)):
        if splited[indx] == '-':
            new_num = calculate(splited[indx - 1], splited[indx + 1], splited[indx])
            splited[indx - 1] = new_num
            del splited[indx:indx + 2]
        elif splited[indx] == '+':
            new_num = calculate(splited[indx - 1], splited[indx + 1], splited[indx])
            splited[indx - 1] = new_num
            del splited[indx:indx + 2]
        if len(splited) == 3:
            flag = False
            break
print(splited)







