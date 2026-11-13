TAVOITE = 500

def lue_tuotanto_data(tiedosto):
    data = []
    with open(tiedosto,"r", encoding="utf-8") as f:
        next(f)
    
        for rivi in f:
            rivi = rivi.strip()
            paiva, maara = rivi.split(",")

            data.append({
                "paiva": paiva,
                "maara": int(maara)
            })
    return data

data = lue_tuotanto_data("data/tuotanto.csv")
def laske_kokonaismaara(lista):
    kokonaismaara = 0
    for rivi in lista:
        kokonaismaara += rivi["maara"]
    return kokonaismaara

def laske_keskiarvo(lista):
    kokonaismaara = 0

    for rivi in lista:
        kokonaismaara += rivi["maara"]
    return kokonaismaara / len(lista)

def laske_maksimi(lista):
    maksimi = lista[0]["maara"]
    for rivi in lista:
        if rivi["maara"] > maksimi:
            maksimi = rivi["maara"]
    return maksimi


def laske_minimi(lista):
    minimi = lista[0]["maara"]
    for rivi in lista:
        if rivi["maara"] < minimi:
            minimi = rivi["maara"]
    return minimi
    

def laske_tehokkuus(lista, tavoite):
    return laske_keskiarvo(lista) / tavoite *100

def paras_paiva(lista):
    paras = lista[0]
    
    for rivi in lista:
        if rivi["maara"] > paras["maara"]:
            paras = rivi
    return paras

def heikoin_paiva(lista):
    heikoin = lista[0]

    for rivi in lista:
        if rivi["maara"] < heikoin["maara"]:
            heikoin = rivi
    return heikoin


def tulosta_raportti(lista, tavoite):
    paras = paras_paiva(lista)
    heikoin = heikoin_paiva(lista)
    print(f"""TUOTANTORAPORTTI

Kokonaismäärä: {laske_kokonaismaara(lista)}
Keskiarvo: {laske_keskiarvo(lista)}
Suurin päivä: {laske_maksimi(lista)}
Pienin päivä: {laske_minimi(lista)}
Tehokkuus: {laske_tehokkuus(lista, tavoite):.1f} %

Paras päivä: {paras["paiva"]} ({paras["maara"]})
Heikoin päivä: {heikoin["paiva"]} ({heikoin["maara"]})
""")


tulosta_raportti(data, TAVOITE)

