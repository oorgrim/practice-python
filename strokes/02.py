# numbers = []
# num_len = int(input("введите размер списка: "))

# for i in range(num_len):

#     number = int(input("Введите число: "))

#     numbers.append(number)
# print(numbers)




# numbers = input("Введите числа через пробел: ").split()
# numbers = [int(num) for num in numbers]

# print(numbers)


input_numbers = input("Введите числа через пробел: ")

input_numbers_list = input_numbers.split()

# Инициализация пустого списка для хранения чисел
numbers = []

# Преобразование строковых значений введенных чисел в целые числа
for num_str in input_numbers_list:
    try:
        # Преобразование строки в целое число и добавление в список
        num = int(num_str)
        numbers.append(num)
    except ValueError:
        # В случае ошибки преобразования (например, если введенное значение не является числом)
        print(f"Ошибка: '{num_str}' не является числом. Пропускаем это значение.")

# Вывод списка чисел
print("Список чисел:", numbers)
