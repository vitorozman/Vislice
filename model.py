import random
import json

ZACETEK = 'Z'

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'

ZMAGA, PORAZ = 'W', 'X'


bazen_besed = []
with open('besede.txt', encoding='UTF-8') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke == None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True
        # all preveri ali so vse stvari v seznamu
        # all(c in self.crke for c in self.geslo) 

    def poraz(self):  
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
       
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
        
    def pravilni_del_gesla(self):
        trenutno = ''
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += '_'
        return trenutno
    
    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(ugibana_crka)
        
        if ugibana_crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ 
            else:
                NAPACNA_CRKA


class Vislice:
    '''
    Skrbi za trenutno stanje VEC iger (imel bo vec objektov tipa Igra)
    '''
    def __init__(self):
        self.igre = {} #slover id-ju priredi igre
        
    def prost_id_igre(self):#vrne nek id ki ga ne uporablja nebona igra
        if len(self.igre) == 0:
            return 0
        else:
            max(self.igre.keys()) + 1

    def nova_igra(self):
        self.preberi_iz_datoteke()
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra()
        self.igre[nov_id] = (sveza_igra, ZACETEK)
        self.shrani_v_datoteko()
        return nov_id

    def ugibaj(self, id_igre, crka):
        self.preberi_iz_datoteke()
        trenutna_igra, _ = self.igre[id_igre]
        novo_staneje = trenutna_igra.ugibaj(crka)
        self.igre[id_igre] = (trenutna_igra, novo_staneje)
        self.shrani_v_datoteko()

    def shrani_v_datoteko(self):
        igre = {}
        for id_igre, (igra, stanje) in self.igre.items(): #id_ogre, (igra, stanje)
            igre[id_igre] = ((igra.geslo, igra.crke), stanje)
        
        with open('stanje_iger.json', 'w') as out_file:
            json.dump(igre, out_file)

    def preberi_iz_datoteke(self):
        with open('stanje_iger.json', 'r') as in_file:
            igre = json.load(in_file)

        self.igre = {}
        for id_igre, ((geslo, crke), stanje) in igre.items():
            self.igre[int(id_igre)] = Igra(geslo, crke), stanje


def nova_igra():
    naklucna_beseda = random.choice(bazen_besed)
    return Igra(naklucna_beseda)

