# Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

#Lietotāju ievade 
lietotaja_ievade = int(input("Ievadiet skaitli: "))

# Saskaitīšanas mainīgais
summa = 0

# For cikls izmantojam mēs, lai saskaitītu no 1 līdz ievadītajam skaitlim
for i in range(1, lietotaja_ievade + 1):
    summa += i

# Izvadē jeb terminālī tiek parādīta saskaitīto skaitļu summa
print(f"Saskaitot no 1 līdz {lietotaja_ievade}, rezultāts ir: {summa}")

