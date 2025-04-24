from algemene_functies import mijn_functie_2 
def aanbieding_1(smaak, prijs, korting):
    korting = prijs * 0.1 
    nieuwe_prijs = prijs - korting
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
print(aanbieding_1("aardbei" , 4 , 0.1))
def inkomsten_totaal(inkomsten , btw):
    totaal = sum(inkomsten )
    btw_bedrag = totaal*btw
    return f"Het totaal van alle inkomsten van deze week is <totaal> euro, waarover <btw_bedrag> euro btw betaald dient te worden."
    week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
    btw_percentage = 0.09
    resultaat = inkomsten_totaal(week_inkomsten , btw_percentage)
    print(resultaat)
def laag_en_hoog():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 34]
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return (hoogste,laagste)
resultaat =  laag_en_hoog()
print(resultaat)
def gemiddelde(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f"de gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."
def meervoudig(invoer_lijst):
    invoer_lijst = [10,5,3,2,1,2,9]
    hoogste = max(invoer_lijst)
    laagste = min(invoer_lijst)
    return (hoogste,laagste)
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2) 
    return mijn_functie_2(korte_lijst)
print(mijn_functie_2)




    