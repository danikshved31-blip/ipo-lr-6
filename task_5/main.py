import random
spisok = []
otricatelnie = 0
polozhitelnie = 0
nulevie = 0
while len(spisok) < 25:
    spisok.append(random.randint(-50, 50))
print(spisok)
for i in spisok:
    if i < 0:
        otricatelnie += 1
    elif i == 0:
        nulevie += 1
    else:
        polozhitelnie += 1
if otricatelnie == 0:
    print("нету отрицательных значений")
else:
    procent_otricatelnih = 25 / otricatelnie * 100
if polozhitelnie == 0:
    print("нету положительных значений")
else:
    procent_polozhitelnih = 25 / polozhitelnie * 100
if nulevie == 0:
    print("нету нулевых значений")
else:
    procent_nulevih = 25 / nulevie * 100
print(f"отрицательных: {otricatelnie} {procent_otricatelnih} , положительных {polozhitelnie}  {procent_polozhitelnih} , нулевых {nulevie} {procent_nulevih} ")
