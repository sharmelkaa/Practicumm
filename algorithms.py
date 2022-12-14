import random
from prettytable import PrettyTable


def data_generator():
    best_case = list(range(100))
    random_case = [random.randint(0, 99) for _ in range(100)]
    worst_case = [i for i in range(99, -1, -1)]
    return best_case, random_case, worst_case


def bubble_sort(lst, count_calc=0, count_equal=0):
    lst_ = lst[:]
    lst_len = len(lst_)
    count_calc += 2

    count_equal += 1
    for index in range(lst_len):
        count_equal += 1
        swapped = False
        count_calc += 2

        count_equal += 1
        for j in range(0, lst_len - index - 1):
            count_equal += 1
            count_calc += 3

            if lst_[j] > lst_[j + 1]:
                count_calc += 1
                count_equal += 1
                lst_[j], lst_[j + 1] = lst_[j + 1], lst_[j]
                swapped = True
                count_calc += 5
            else:
                count_calc += 1
                count_equal += 1

        count_equal += 1
        if not swapped:
            break

    return count_equal, count_calc


def insertion_sort(lst, count_calc=0, count_equal=0):
    lst_ = lst[:]
    lst_len = len(lst_)
    count_calc += 2

    count_equal += 1
    for index in range(1, lst_len):
        count_equal += 1
        item_to_insert = lst_[index]
        prev_elem_index = index - 1
        count_calc += 3

        while prev_elem_index >= 0 and lst_[prev_elem_index] > item_to_insert:
            count_equal += 2
            lst_[prev_elem_index + 1] = lst_[prev_elem_index]
            prev_elem_index = prev_elem_index - 1
            count_calc += 3
        count_equal += 2

        lst_[prev_elem_index + 1] = item_to_insert
        count_calc += 2

    return count_equal, count_calc


def cocktail_sort(lst, count_calc=0, count_equal=0):
    lst_ = lst[:]
    lst_len = len(lst_)
    start = 0
    end = lst_len - 1
    swapped = True
    count_calc += 5

    while swapped:
        count_equal += 1
        swapped = False
        count_calc += 1

        count_equal += 1
        for index in range(start, end):
            count_equal += 1
            count_calc += 1

            if lst_[index] > lst_[index + 1]:
                count_equal += 1
                count_calc += 1
                lst_[index], lst_[index + 1] = lst_[index + 1], lst_[index]
                swapped = True
                count_calc += 5
            else:
                count_calc += 1
                count_equal += 1

        count_equal += 1
        if not swapped:
            break

        swapped = False
        end = end - 1
        count_calc += 2

        count_equal += 1
        for index in range(end - 1, start - 1, -1):
            count_equal += 1
            count_calc += 3

            if lst_[index] > lst_[index + 1]:
                count_calc += 1
                lst_[index], lst_[index + 1] = lst_[index + 1], lst_[index]
                swapped = True
                count_calc += 5
            else:
                count_calc += 1
                count_equal += 1
    count_equal += 1

    return count_equal, count_calc


def shell_sort(lst, count_calc=0, count_equal=0):
    lst_ = lst[:]
    lst_len = len(lst_)
    gap = lst_len // 2
    count_calc += 3

    while gap > 0:
        count_equal += 1

        count_equal += 1
        for index in range(gap, lst_len):
            count_equal += 1
            temp = lst_[index]
            j = index
            count_calc += 3
            while j >= gap and lst_[j - gap] > temp:
                count_equal += 2
                lst_[j] = lst_[j - gap]
                j -= gap
                count_calc += 4
            count_calc += 1
            count_equal += 2

            lst_[j] = temp
            count_calc += 1

        gap //= 2
        count_calc += 1
    count_equal += 1

    return count_equal, count_calc


count_equal_qs = 0
count_calc_qs = 0


def quick_sort(lst):
    global count_calc_qs
    global count_equal_qs

    lst_ = lst[:]
    lst_len = len(lst_)
    count_calc_qs += 2

    quick_sort_helper(lst, 0, lst_len - 1)
    count_calc_qs += 1

    return count_equal_qs, count_calc_qs


def quick_sort_helper(lst, first, last):
    global count_equal_qs
    global count_calc_qs

    lst_ = lst[:]
    count_calc_qs +=1

    if first < last:
        count_equal_qs += 1

        splitpoint = partition(lst_, first, last)
        quick_sort_helper(lst_, first, splitpoint - 1)
        quick_sort_helper(lst_, splitpoint + 1, last)
        count_calc_qs += 3
    else:
        count_equal_qs += 1


def partition(lst, first, last):
    global count_calc_qs
    global count_equal_qs

    lst_ = lst[:]
    pivot_value = lst_[first]
    left_mark = first + 1
    right_mark = last
    done = False
    count_calc_qs += 5

    while not done:
        count_equal_qs += 1

        while left_mark <= right_mark and lst_[left_mark] <= pivot_value:
            count_equal_qs += 2
            left_mark = left_mark + 1
            count_calc_qs += 1
        count_equal_qs += 2

        while lst_[right_mark] >= pivot_value and right_mark >= left_mark:
            count_equal_qs += 2
            right_mark = right_mark - 1
            count_calc_qs += 1
        count_equal_qs += 2

        if right_mark < left_mark:
            count_equal_qs += 1
            done = True
            count_calc_qs += 1
        else:
            count_equal_qs += 1
            temp = lst_[left_mark]
            lst_[left_mark] = lst_[right_mark]
            lst_[right_mark] = temp
            count_calc_qs += 3
    count_equal_qs += 1

    temp = lst_[first]
    lst_[first] = lst_[right_mark]
    lst_[right_mark] = temp
    count_calc_qs += 3

    return right_mark


result = PrettyTable()
result.add_column('',
                  ['Сортировка пузырьком',
                   'Сортировка вставками',
                   'Шейкер-сортировка',
                   'Сортировка Шелла',
                   'Быстрая сортировка'])

field_names = ['Отсортированный список', 'Псевдо-случайный список', 'Отсортированный в обратную сторону список']

index = 0
for case in data_generator():
    result.add_column(field_names[index],
                      [str(bubble_sort(case))[1:-1],
                       str(insertion_sort(case))[1:-1],
                       str(cocktail_sort(case))[1:-1],
                       str(shell_sort(case))[1:-1],
                       str(quick_sort(case))[1:-1]])
    index += 1
print(result)
