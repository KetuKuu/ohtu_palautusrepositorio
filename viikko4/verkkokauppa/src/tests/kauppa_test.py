import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

            if tuote_id == 2:
                return 10
            
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
            if tuote_id == 2:
                return Tuote(2, "leipä", 2)
            
            if tuote_id == 3:
                return Tuote(1, "kala", 10)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_ostoksen_paaytyttya_kaksi_eri_tuotetta_korissa_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.lisaa_koriin(2)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 7) 

    def test_ostoksen_paaytyttya_kaksi_samaa_tuotetta_korissa_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 10) 

    def test_ostoksen_paaytyttya_yksi_tuote_loppu_toinen_tuote_korissa_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.lisaa_koriin(3)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)  

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 2) 

    def test_uusi_viite_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.assert_called()

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.assert_called()

    def test_tuotteen_lisaaminen_koriin_ei_onnistu_jos_saldo_on_nolla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 0)

    def test_saman_tuotteen_poistaminen_korista_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.poista_korista(1)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 0)

    def test_tuotteen_lisaaminen_koriin_ei_onnistu_kun_saldo_on_nolla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)  
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 0) 