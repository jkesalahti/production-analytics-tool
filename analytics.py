"""Talouden tunnuslukujen laskemiseen käytettäviä funktioita"""

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
    
def laske_liikevaihto(lista, myyntihinta):
    return laske_kokonaismaara(lista) * myyntihinta
        

def laske_kustannukset(lista, valmistuskustannus):
    return laske_kokonaismaara(lista) * valmistuskustannus

def laske_kate(lista, myyntihinta, valmistuskustannus):
    return laske_liikevaihto(lista, myyntihinta) - laske_kustannukset(lista, valmistuskustannus)    
    
def laske_tehdaskohtaiset_maarat(lista):
    tehtaat = {}
    for rivi in lista:
        if rivi["tehdas"] not in tehtaat:
            tehtaat[rivi["tehdas"]] = rivi["maara"]
        else:
            tehtaat[rivi["tehdas"]] += rivi["maara"]
            
    return tehtaat
    
def paras_tehdas(lista):
    tehtaat = laske_tehdaskohtaiset_maarat(lista)
    
    paras_nimi = ""
    suurin_maara = 0
    
    
    for tehdas in tehtaat:
        if tehtaat[tehdas] > suurin_maara:
            suurin_maara = tehtaat[tehdas]
            paras_nimi = tehdas
    
    return paras_nimi, suurin_maara


def heikoin_tehdas(lista):
    tehtaat = laske_tehdaskohtaiset_maarat(lista)
    
    heikoin_nimi = ""
    pienin_maara = None
    
    for tehdas in tehtaat:
        if pienin_maara is None or tehtaat[tehdas] < pienin_maara:
            pienin_maara = tehtaat[tehdas]
            heikoin_nimi = tehdas
    
    return heikoin_nimi, pienin_maara

