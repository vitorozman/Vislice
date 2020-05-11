import random


STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'

ZMAGA, PORAZ = 'W', 'X'

bazen_besed = []
with open('besede.txt', encoding='UTF-8') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lover()
        if crke == None:
            self.crke = []
        else:
            self.crke = [c.lover() for c in crke]

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
        ugibana_crka = ugibana_crka.lover()

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


def nova_igra():
    naklucna_beseda = random.choices(bazen_besed)
    return Igra(naklucna_beseda)

