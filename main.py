from analytics import *

TAVOITE = 500
MYYNTIHINTA = 15
VALMISTUSKUSTANNUS = 9

def lue_tuotanto_data(tiedosto):
    data = []
    with open(tiedosto,"r", encoding="utf-8") as f:
        next(f)
    
        for rivi in f:
            rivi = rivi.strip()
            tehdas, paiva, maara = rivi.split(",")

            data.append({
                "tehdas": tehdas,
                "paiva": paiva,
                "maara": int(maara)
            })
    return data



def tulosta_raportti(lista, tavoite, myyntihinta, valmistuskustannus):
    paras = paras_paiva(lista)
    heikoin = heikoin_paiva(lista)
    paras_nimi, paras_maara = paras_tehdas(lista)
    heikoin_nimi, heikoin_maara = heikoin_tehdas(lista)
    print(f"""TUOTANTORAPORTTI

Kokonaismäärä: {laske_kokonaismaara(lista)}
Keskiarvo: {laske_keskiarvo(lista)}
Suurin päivä: {laske_maksimi(lista)}
Pienin päivä: {laske_minimi(lista)}
Tehokkuus: {laske_tehokkuus(lista, tavoite):.1f} %

Paras päivä: {paras["paiva"]} ({paras["maara"]})
Heikoin päivä: {heikoin["paiva"]} ({heikoin["maara"]})

TALOUS

Liikevaihto: {laske_liikevaihto(lista, myyntihinta)} €
Kustannukset: {laske_kustannukset(lista, valmistuskustannus)} €
Kate: {laske_kate(lista, myyntihinta, valmistuskustannus)} €

TEHTAIDEN YHTEENVETO

Paras tehdas: {paras_nimi} ({paras_maara})
Heikoin tehdas: {heikoin_nimi} ({heikoin_maara})
""")

if __name__ == "__main__":
    data = lue_tuotanto_data("data/tuotanto.csv")
    tulosta_raportti(
    data,
    TAVOITE,
    MYYNTIHINTA 
    VALMISTUSKUSTANNUS
)

        
