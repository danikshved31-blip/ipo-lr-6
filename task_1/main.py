# Создаем список из 6 строк
strings_list = [
    "Привет, мир!",
    "Python - это круто",
    "Программирование весело",
    "Учусь кодить",
    "Списки в Python",
    "Последняя строка"
]
d = "д"
summa = 0
# Выводим список
print("Список строк:")
for i in strings_list:
    print(i)
for i in strings_list:
    if d in i:
        summa +=1
print(summa)
