def audio_file_duration(disk_space, bits_per_sample, sample_rate):
    return (disk_space * 1024 * 8 * bits_per_sample) / (sample_rate * bits_per_sample * sample_rate)

disk_space = float(input("Введите объём свободной памяти на диске (ГБ): "))
bits_per_sample = int(input("Введите разрядность звуковой платы (бит): "))
sample_rate = int(input("Введите частоту дискретизации (Гц): "))

print("Длительность звучания:", audio_file_duration(disk_space, bits_per_sample, sample_rate), "сек")