import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_löytää_pelaajan(self):
        pelaaja = self.stats.search("Lemieux")
        self.assertIsNotNone(pelaaja)
        self.assertEqual(pelaaja.name, "Lemieux")

    def test_haku_palauttaa_none_jos_ei_löydy(self):
        pelaaja = self.stats.search("Tuntematon")
        self.assertIsNone(pelaaja)

    def test_tiimi_palauttaa_oikeat_pelaajat(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)  
        self.assertTrue(all(pelaaja.team == "EDM" for pelaaja in pelaajat))




    def test_top_points_palauttaa_oikean_määrän_pelaajia(self):
        parhaat_pelaajat = self.stats.top(2, sort_by="points")
        self.assertEqual(len(parhaat_pelaajat), 2)

    def test_top_goals_palauttaa_oikeat_pelaajat(self):
        parhaat_pelaajat = self.stats.top(2, sort_by="goals")
        odotetut_nimet = ["Gretzky", "Lemieux"]
        self.assertEqual([pelaaja.name for pelaaja in parhaat_pelaajat], odotetut_nimet)

    def test_top_assists_palauttaa_oikeat_pelaajat(self):
        parhaat_pelaajat = self.stats.top(2, sort_by="assists")
        odotetut_nimet = ["Gretzky", "Yzerman"]
        self.assertEqual([pelaaja.name for pelaaja in parhaat_pelaajat], odotetut_nimet)