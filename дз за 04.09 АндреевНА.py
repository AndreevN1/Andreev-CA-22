import math

def task18(bytesonpages, numpages, rowsonpages, symbolsonpage):
    i = (bytesonpages * numpages) / (rowsonpages*symbolsonpage)
    return int(i)

def task19(firstsize, secondsize, textlen):
    firstinfo = textlen * math.log2(firstsize)
    secondinfo = textlen * math.log2(secondsize)
    difference = secondinfo / firstinfo
    return difference

def task20(alpsize, bitsize):
    bitpersym = bitsize / math.log2(alpsize)
    return int(bitpersym)

def task19_2(bit):
    housefloor = 2 ** bit
    return int(housefloor)

def task20_2(b, N):  
    i = math.log2(N)
    allN = 2 ** N
    return int(allN)

def task7(whitebit, bluepaint):
    bluebit = whitebit 
    totalblueinfo = bluebit * bluepaint
    brownpaint = totalblueinfo / whitebit
    return int(brownpaint)

if __name__ == "__main__":

    # inp1 = int(input("Введите кол-во байт "))
    # inp2 = int(input("Введите кол-во страниц "))
    # inp3 = int(input("Введите кол-во строк "))
    # inp4 = int(input("Введите кол-во символов в строке "))
    # print(task18(inp1, inp2, inp3, inp4), "Количество символов в алфавите ")

    # inp5 = int(input("Введите мощность первого алфавита"))
    # inp6 = int(input("Введите мощность второго алфавита "))
    # inp7 = int(input("Введите длину текста "))
    # print(task19(inp5, inp6, inp7), "Разница в количестве информации ")

    #  inp8 = int(input("Введите мощность алфавита "))
    #  inp9 = int(input("Введите кол-во бит в сообщении "))
    #  print(task20(inp8, inp9), "Количество символов в сообщении ")

    # inp10 = int(input("Введите количество бит информации "))
    # print(task19_2(inp10), "Количество этажей в доме ")

    # inp11 = int(input("Введите кол-во бит информации "))
    # inp12 = int(input("Введите кол-во подъездов "))
    # print(task20_2(inp12), "Количество подъездов в доме ")

    # inp13 = int(input("Введите количество бит информации о том что закончилась белая краска "))
    # inp14 = int(input("Введите израсходавали синей краски "))
    # print(task7(inp13, inp14), "банок коричневой краски ")