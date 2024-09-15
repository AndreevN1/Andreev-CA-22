def to_decimal(num, base):
    result = 0
    while num:
        result += num % 10 * (base ** (len(str(num)) - 1 - num % 10))
        num //= 10
    return result

def from_decimal_to_other(number, base_from, base_to):
    if base_from == 10:
        number = to_decimal(number, base_from)
    remainder = number % base_to
    quotient = number // base_to
    res = remainder
    while quotient:
        remainder = quotient % base_to
        quotient //= base_to
        res = base_to * res + remainder
    return res


base_from = int(input("Введите исходную систему счисления: "))
number = float(input("Введите число: "))


base_to = int(input("Введите целевую систему счисления: "))

print("Число", number, "в системе счисления с основанием", base_from, "равно", to_decimal(number, base_from), "в десятичной системе счисления.")
print("Это число равно", from_decimal_to_other(to_decimal(number, base_from), 10, base_to), "в системе счисления с основанием", base_to)
