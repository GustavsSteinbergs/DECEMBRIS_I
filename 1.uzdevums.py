# Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.


lietotaja_ievade = int(input("Ievadiet skaitli: "))
summa = 0

for i in range(1, lietotaja_ievade + 1):
    summa += i

print(f"Saskaitot no 1 līdz {lietotaja_ievade}, rezultāts ir: {summa}")
