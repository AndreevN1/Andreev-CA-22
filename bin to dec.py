def binary_to_decimal(binary_num):
    binary_list = list(binary_num)
    decimal_value = 0
    power = len(binary_list) - 1
    for i in range(len(binary_list)):
        if binary_list[i] == '1':
            decimal_value += 2 ** power
        power -= 1

    fractional_part = 0.0
    for i in reversed(range(len(binary_list))):
        if binary_list[i] != '0':
            fractional_part += (2 * (1 / 2) ** i)

    return decimal_value + fractional_part

binary_number = input("Введите двоичное число: ")
decimal_number = binary_to_decimal(binary_number)
print("Двоичное число", binary_number, "равно десятичному числу", decimal_number)
