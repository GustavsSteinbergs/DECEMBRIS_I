# Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis dalās ar 3 un 7, izmantojot if priekšrakstu.

# Ievadu
skaitlis = int(input("Ievadiet skaitli: "))

# Pārbaudu, vai skaitlis dalās ar 3 un 7
if skaitlis % 3 == 0 and skaitlis % 7 == 0:
    print(f"{skaitlis} dalās gan ar 3, gan ar 7.")
else:
    print(f"{skaitlis} nedalās gan ar 3, gan arī ar 7.")
