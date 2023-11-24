# Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu (labrīt, labdien, labvakar).

import datetime

def sveiciens_pēc_stundas():
    stunda = datetime.datetime.now().hour

    if 5 <= stunda < 12:
        return "Labrīt!"
    elif 12 <= stunda < 18:
        return "Labdien!"
    else:
        return "Labvakar!"

# Sveiciens
print(sveiciens_pēc_stundas())
