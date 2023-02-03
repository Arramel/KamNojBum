import random
print("Добро пожаловать в игру!")
change = ["камень", "ножницы", "бумага"]

while True:
    hod = input("Введите камень, ножницы или бумага: ").lower()
    sop = random.choice(change)
    if hod == "стоп":
        print("остановка")
        break

    if hod == "камень" or hod == "ножницы" or hod == "бумага":
        print("Начинаем игру! Ваш ход:", hod)
        print("Ход соперника:", sop)
    else:
        print("Вы ввели что-то не так!")
        continue

    if hod == sop:
        print("Ничья!")
    elif hod == "камень" and sop == "ножницы":
        print("Вы победили!")
        break
    elif hod == "ножницы" and sop == "бумага":
        print("Вы победили!")
        break
    elif hod == "бумага" and sop == "камень":
        print("Вы победили!")
        break
    else:
        print("Вы проебали!")
        break


