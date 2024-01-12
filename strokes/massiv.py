
input_numbers = input("Введите числа через пробел: ")

input_numbers_list = input_numbers.split()

numbers = []

for num_str in input_numbers_list:
    try:
        num = int(num_str)
        numbers.append(num)
    except ValueError:
        print(f"Ошибка: '{num_str}' не является числом. Пропускаем это значение.")

print("Список чисел:", numbers)