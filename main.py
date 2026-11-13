TAVOITE = 500

def lue_tuotanto_data(tiedosto):
    lista = []
    with open(tiedosto,"r", encoding="utf-8") as f:
        data = f.read().splitlines()
        for rivi in data:
            lista.append(int(rivi))
    return lista

def laske_kokonaismaara(lista):
    return sum(lista)

def laske_keskiarvo(lista):
    return sum(lista) / len(lista)

def laske_maksimi(lista):
    return max(lista)

def laske_minimi(lista):
    return min(lista)

def laske_tehokkuus(lista, tavoite):
    return laske_keskiarvo(lista) / tavoite *100

def tulosta_raportti(lista, tavoite):
    print(f"""TUOTANTORAPORTTI

    Kokonaismäärä: {laske_kokonaismaara(lista)}
    Keskiarvo: {laske_keskiarvo(lista)}
    Suurin päivä: {laske_maksimi(lista)}
    Pienin päivä: {laske_minimi(lista)}
    Tehokkuus: {laske_tehokkuus(lista, tavoite):.1f} %""")

tuotanto = lue_tuotanto_data("data/tuotanto.txt")
tulosta_raportti(tuotanto, TAVOITE)
