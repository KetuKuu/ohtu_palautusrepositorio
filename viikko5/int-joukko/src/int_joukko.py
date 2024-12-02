KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
        
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti if isinstance(kapasiteetti, int) and kapasiteetti > 0 else self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if isinstance(kasvatuskoko, int) and kasvatuskoko > 0 else self.OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti <= 0:
            raise ValueError("Kapasiteetin on oltava positiivinen kokonaisluku")

        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko <= 0:
            raise ValueError("Kasvatuskoon on oltava positiivinen kokonaisluku")

        self.lista = self._luo_lista(self.kapasiteetti)
        self.seuraava_alkio = 0

    def kuuluu(self, n):

        for i in range(self.seuraava_alkio):
            if n == self.lista[i]:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False 

        if self.seuraava_alkio >= len(self.lista):
            self._kasvata_kapasiteettia()

        self.lista[self.seuraava_alkio] = n
        self.seuraava_alkio += 1
        return True

    def _kasvata_kapasiteettia(self):
        uusi_lista = self._luo_lista(len(self.lista) + self.kasvatuskoko)
        self.kopioi_lista(self.lista, uusi_lista)
        self.lista = uusi_lista

    def poista(self, n):
        for i in range(self.seuraava_alkio):
            if self.lista[i] == n:
                self.siirra_vasemmalle(i)
                self.seuraava_alkio -= 1
                return True
        return False
    
    def siirra_vasemmalle(self, index):
        for i in range(index, self.seuraava_alkio - 1):
            self.lista[i] = self.lista[i + 1]
        self.lista[self.seuraava_alkio - 1] = 0

    def kopioi_lista(self, listatsta, listaan):
        for i in range(0, len(listatsta)):
            listaan[i] = listatsta[i]

    def mahtavuus(self):
        return self.seuraava_alkio

    def to_int_list(self):
        return self.lista[:self.seuraava_alkio]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()

        for alkio in a.to_int_list():
            yhdiste.lisaa(alkio)

        for alkio in b.to_int_list():
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        uusi_lista = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio_a in a_taulu:
            if alkio_a in b_taulu:
                uusi_lista.lisaa(alkio_a)

        return uusi_lista

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            erotus.lisaa(alkio)

        for alkio in b_taulu:
            erotus.poista(alkio)

        return erotus

    def __str__(self):
        if self.seuraava_alkio == 0:
            return "{}"
        
        return "{" + ", ".join(map(lambda num: str(num), self.lista[:self.seuraava_alkio])) + "}"
