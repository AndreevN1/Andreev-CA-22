V = float(input("Введите объём аудиофайла (в Кб): "))  # запрашиваем у пользователя объём аудиофайла
b = 16  # разрядность звуковой платы равна 16
Fs = 32000  # частота дискретизации равна 32 кГц

t = V * b / Fs / 1024 # Расчёт времени звучания

print("Время звучания:", t, "с")