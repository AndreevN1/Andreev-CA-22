colors = int(input("Введите количество цветов в рисунке: "))
memory_size = int(input("Сколько байт информации содержит рисунок? "))

bits_per_pixel = memory_size * 8 // colors  # вычисляем количество бит, которое приходится на один пиксель
points = colors ** bits_per_pixel  # находим общее количество точек в рисунке

print("Рисунок состоит из", points, "точек")