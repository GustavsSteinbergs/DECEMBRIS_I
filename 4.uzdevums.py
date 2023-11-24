 # Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.

def faktorials(skaitlis):
    rezultats = 1
    for i in range(1, skaitlis + 1):
        rezultats *= i
    return rezultats

# Ievadītais skaitlis
ievaditais_skaitlis = int(input("Ievadiet skaitli, kura faktoriālu vēlaties aprēķināt: "))

# Rezultāta ieguve
print(f"Faktoriāls no {ievaditais_skaitlis} ir: {faktorials(ievaditais_skaitlis)}")
