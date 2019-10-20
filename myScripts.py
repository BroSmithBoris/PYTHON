from random import uniform
from struct import pack
from struct import unpack


# Создание списка случайных значений
# list_size - размер списка
# mim_value - минимальное значение
# max_value - максимальное значение
def list_numbers_creation(min_value, max_value):
    new_list = []
    for i in range(list_size):
        new_list.append(uniform(min(min_value, max_value), max(min_value, max_value)))
    print(new_list)
    return new_list


# Создание битового файла на базе списка значений
# list - список значений
def file_bit_numbers_creation(list):
    file = open('BITS.bin', 'w+b')
    for i in list:
        file.write(pack('d', i))
    return file


# Чтение битового файла значений
# file - битовый файл значений
def file_bit_numbers_read(file):
    file.seek(0)
    return list(unpack(str(list_size) + 'd', file.read()))


# Анализ битового файла значений
# file - битовый файл значений
def file_bit_analysis(file):
    new_list_numbers = file_bit_numbers_read(file)
    new_list_numbers.sort()
    min_value = min(new_list_numbers)
    max_value = max(new_list_numbers)
    index = int(list_size / 2)
    if list_size % 2 == 0:
        median = (new_list_numbers[index - 1] + new_list_numbers[index]) / 2
    else:
        median = new_list_numbers[index]
    average = sum(new_list_numbers) / list_size
    new_analysis_list = [min_value, max_value, median, average]
    return new_analysis_list


# Создание битового файла на основе анализа значений
# list - список созданный на основе анализа значений
def file_bit_analysis_creation(list):
    file = open('ANALYTICS.bin', 'w+b')
    for i in list:
        file.write(pack('d', i))
    return file


# Чтение битового файла анализа
# file - битовый файл анализа
def file_bit_analysis_read(file):
    file.seek(0)
    return list(unpack('4d', file.read()))


list_size = int(input('Размер списка: '))
list_numbers = list_numbers_creation(int(input('Минимальное значение: ')), int(input('Максимальное значение: ')))
print(list_numbers)

file_bit_numbers = file_bit_numbers_creation(list_numbers)
file_bit_numbers.seek(0)
print(file_bit_numbers)

list_numbers = file_bit_numbers_read(file_bit_numbers)
print(list_numbers)

analysis_list = file_bit_analysis(file_bit_numbers)
print(analysis_list)

file_bit_analysis = file_bit_analysis_creation(analysis_list)
file_bit_analysis.seek(0)
print(file_bit_analysis.read())

analysis_list = file_bit_analysis_read(file_bit_analysis)
print(analysis_list)

file_bit_numbers.close()
file_bit_analysis.close()
