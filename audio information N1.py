def audio_file_size(sample_rate, bits_per_sample, duration):  # Определяем функцию audio_file_size, которая принимает три аргумента: sample_rate (частота дискретизации в Гц), bits_per_sample (разрешение в битах) и duration (время звучания в секундах). Функция возвращает объём памяти в килобайтах, необходимый для хранения цифрового аудиофайла.
    return (sample_rate * bits_per_sample * duration) / (8 * 1024)  # Рассчитываем объём памяти, умножая sample_rate, bits_per_sample и duration

sample_rate = int(input("Введите частоту дискретизации (Гц): "))  
bits_per_sample = int(input("Введите разрешение (бит): "))  
duration = float(input("Введите время звучания (сек): "))  
print("Объём памяти:", audio_file_size(sample_rate, bits_per_sample, duration), "KB") 