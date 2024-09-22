import math
old_colors = int(input("Введите количество цветов до преобразования: "))
new_colors = int(input("Введите новое количество цветов: "))

bits_per_pixel_old = old_colors * math.log(2, old_colors)  # формула для определения количества бит, необходимых для кодирования одного пикселя при старом количестве цветов
bits_per_pixel_new = new_colors * math.log(2, new_colors) # формула для определения количества бит, необходимых для кодирования одного пикселя при новом количестве цветов

bytes_per_pixel_old = bits_per_pixel_old // 8  # переводим в байты
bytes_per_pixel_new = bits_per_pixel_new // 8

increase_factor = bytes_per_pixel_new / bytes_per_pixel_old

print("Объём памяти увеличился в", increase_factor, "раз")