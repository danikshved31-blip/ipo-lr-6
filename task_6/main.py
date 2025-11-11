import random

# Создаем случайный список из 20 значений в диапазоне от -10 до 10
spisok = []
while len(spisok) < 20:
    spisok.append(random.randint(-10, 10))

# Выводим сгенерированный список
print("Сгенерированный список:", spisok)

# Находим все уникальные комбинации из 2 элементов (пары)
# Используем set для устранения дубликатов, sorted для игнорирования порядка
unikalnye_pary = set()
for i in range(len(spisok)):
    for j in range(i + 1, len(spisok)):
        # Сортируем пару, чтобы (a,b) и (b,a) считались одинаковыми
        para = tuple(sorted([spisok[i], spisok[j]]))
        unikalnye_pary.add(para)

# Преобразуем множество обратно в список кортежей
spisok_kortezhey = list(unikalnye_pary)

# Выводим все уникальные комбинации
print("Уникальные комбинации (пары):")
for kortezh in spisok_kortezhey:
    print(kortezh)

# Пользователь вводит целое число
chislo_polzovatelya = int(input("Введите целое число: "))

# Считаем количество пар, чья сумма меньше заданного числа
kolichestvo_par = 0
for para in spisok_kortezhey:
    if sum(para) < chislo_polzovatelya:
        kolichestvo_par += 1

# Выводим результат
print(f"Количество пар, чья сумма меньше {chislo_polzovatelya}: {kolichestvo_par}")
