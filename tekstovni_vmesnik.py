import model


def izpis_poraza(igra):
    return f'IZGUBIL SI, geslo je bilo: {igra.geslo}'

def izpis_zmaga(igra):
    return f'ZMAGAL SI, geslo je bilo: {igra.geslo}'

def izpis_igre(igra):
    text = (
        f'Stanje gesla: {igra.pravilni_del_gesla()} '
        f'Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako'
    )
    return text

def zahtevaj_vnos():
    return input('Vpisi nasledno crko: ')

def pozeni_vmesnik():
    trenutna_igra = model.nova_igra()

    while True:
        print(izpis_igre(trenutna_igra))
        
        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)
        if trenutna_igra.zmaga():
            print(izpis_zmaga(trenutna_igra))
            return
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            return


pozeni_vmesnik()
