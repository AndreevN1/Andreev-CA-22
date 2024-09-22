
ascii_dict = {chr(i): format(i, '016b') for i in range(65536)}

def encode_sentence(sentence):
    binary_code = ''
    for char in sentence:
        binary_code += ascii_dict[char] + ' '
    return binary_code.strip()

sentence = input("введите предложение: ")

print("Двоичный код: ", encode_sentence(sentence))