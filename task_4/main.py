text = input("введите текст который будем искать: ")
spisok = []
sum_strok = 0
with open('text.txt', 'r', encoding=' utf-8 ') as a:
    lines = a.readlines()
    for line in lines:
        if text in line:
            spisok.append(line.strip())
            sum_strok += 1
spisok.sort(key=len)
print(spisok)
print(f"строчек с этим текстом {sum_strok}")
