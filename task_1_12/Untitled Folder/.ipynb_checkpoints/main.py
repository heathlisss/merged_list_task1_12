# ----------------------------------------------------------------------------------------------------------------------
#   Составить новый список чисел из двух переданных списков следующим образом.
#   На нечётные позиции ставить элементы из первого списка, на чётные – из второго.
#   В случае, если один список короче другого, то на недостающие позиции (неважно, четные или нечетные)
#   ставить элементы из более длинного списка (т.е. итоговый список обязательно будет длиной,
#   равной длине более длинного списка), например:
#  1. ({ 1, 2, 3, 4 }, { 101, 102, 103, 104, 105, 106, 107 }) → { 1, 102, 3, 104, 105, 106, 107 }
#  2. вторая версия { 1, 101, 2, 102, 3, 103, 4, 104, 105, 106, 107 }
# ----------------------------------------------------------------------------------------------------------------------

def read_lists_from_file(file_name):
    with open(file_name, 'r') as file:  # открывает файл только для чтения('r')
        lines = file.readlines()
        list1 = [int(num) for num in lines[0].split()]  # проходит по числам строки и записывает их в список
        list2 = [int(num) for num in lines[1].split()]
    return list1, list2  # возвращает кортеж из 2х списков


def merge_lists(list1, list2):
    result = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        if i < len(list1) and i < len(list2):
            if i % 2 == 0:
                result.append(list1[i])
            if i % 2 == 1:
                result.append(list2[i])
        else:
            if i < len(list1):
                result.append(list1[i])
            if i < len(list2):
                result.append(list2[i])
    return result


def merge_all_elements_into_a_list(list1, list2):
    result = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    return result


def write_list_to_file(result_list, file_name):
    with open(file_name, 'w') as file:
        file.write(' '.join(map(str, result_list)))


print('Выберите вариантслияния (1 или 2): ')
flag = input()
print(flag)
list1, list2 = read_lists_from_file('test1.txt')
result_list = []
if flag == '1':
    result_list = merge_lists(list1, list2)
    write_list_to_file(result_list, 'merged_list_1.txt')
elif flag == '2':
    result_list = merge_all_elements_into_a_list(list1, list2)
    write_list_to_file(result_list, 'merged_list_2.txt')
else:
    print('не верные данные')
