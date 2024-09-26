def ShennonFano(array, left, right, border_array):
    """
    Рекурсивно строит коды Шеннона-Фано для элементов массива.

    Args:
        array (list): Список элементов вида [символ, частота, код].
        left (int): Индекс левой границы текущего подмассива.
        right (int): Индекс правой границы текущего подмассива.
        border_array (list): Список индексов границ для рекурсивных вызовов.
    """

    border_array = border_array + [right]
    border = delit(array, left, right)

    for i in array[left:border + 1]:
        i[2] += "1"

    for i in array[border + 1:]:
        i[2] += "0"

    if len(array[left:border + 1]) == 1:
        return

    if len(array[border + 1:]) == 1:
        return

    ShennonFano(array, left, border, border_array)
    ShennonFano(array, border + 1, right, border_array)


def delit(array, left, right):
    """
    Находит индекс, разделяющий массив на две части с примерно равными суммами частот.

    Args:
        array (list): Список элементов вида [символ, частота, код].
        left (int): Индекс левой границы.
        right (int): Индекс правой границы.

    Returns:
        int: Индекс разделителя.
    """

    sum_left = array[left][1]
    sum_right = array[right][1]

    while left + 1 < right:  # Исправлено условие цикла
        if sum_right <= sum_left:
            right -= 1
            sum_right += array[right][1]
        else:
            left += 1
            sum_left += array[left][1]

    return left


if __name__ == "__main__":
    array = [["a", 3, ""], ["b", 3, ""], ["c", 3, ""], ["d", 3, ""]]
    ShennonFano(array, 0, len(array) - 1, [])
    
    print("Коды Шеннона-Фано:")
    for item in array:
        print(item)