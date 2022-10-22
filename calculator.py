# easy = '10 + 0x1'
# for sym in easy.split():
#     if sym in ['+', '-', '*', '/',  '**']:
#         pass
#         #  функции для каждого кто что вычисляет
#     elif sym.isdigit():
#         pass
#         #  интуем
#     elif sym[:2] == '0o':
#         pass
#         #  конвертируем в инт
#     elif sym[:2] == '0x':
#         pass
#         #  конвертируем в инт
#     else:
#         pass
#         #  исключение, валидация


# example = '2 * ((2 + 2) * 2 ** (1 + 0o3))'
# print(example.split())
# new = []
# index_start = 0
# start = 0
# for i_sym in range(0, len(example)):
#     if example[i_sym].isdigit():
#         if example[i_sym] == 0:
#             if example[i_sym+1] == 'o':
#
#             elif example[i_sym] == 'x':
#
#
#     elif sym in ['+', '-', '*', '/',  '**']:
#         pass
#     else:
#         new.append(sym)
# print(new)

easy = '10+ 0x1**2'
# easy = '2 * ((2 + 2) * 2 ** (1 + 0o3))'
num = ''
priority = {'**': 1, '*': 2, '/': 2, '+': 3, '-': 3}
for index in range(0, len(easy)):
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
a = num.split()
for ssym in range(0, len(a)):
    if a[ssym].isdigit():
        a[ssym] = int(a[ssym])
    elif a[ssym].startswith('0x'):
        a[ssym] = int(a[ssym], 16)
    elif a[ssym].startswith('0o'):
        a[ssym] = int(a[ssym], 8)

print(a)



