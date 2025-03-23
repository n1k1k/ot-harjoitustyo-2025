import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # Kassapäätteen rahamäärä alussa oikein
    def test_konstruktori_asettaa_rahan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    # Loundaiden märää alussa 0
    def test_edulliset_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_alussa_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Käteistosto toimii sekä edullisten että maukkaiden lounaiden osalta
    # Jos maksu riittävä: kassassa oleva rahaäärä vaihtorahan suuruus oikea
    def test_kateismaksu_kasvattaa_rahamaaraa_oikein_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)

    def test_kateismaksu_vaihtoraha_oikein_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateismaksu_kasvattaa_rahamaaraa_oikein_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)

    def test_kateismaksu_vaihtoraha_oikein_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    # Lounaiden määrä kasvaa jos maksu onnistuu
    def test_lounaiden_maara_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_lounaiden_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Jos maksu ei ole riittävä kassan rahamäärä ei muutu
    def test_rahamaara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_rahamaara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    # Jos maksu ei riitä kaikki rahat palautetaan vaihtorahana
    def test_kaikki_rahat_palautetaan_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kaikki_rahat_palautetaan_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    # Syötyjen lounaiden määrä ei muutu, jos maksu ei ole riittävä
    def test_lounaiden_maara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lounaiden_maara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Jos kortilla rahaa tarpeeksi, summma veloitetaan kortilta ja palautetaan True
    def test_veloitus_kortilta_oikein_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_veloitus_kortilta_oikein_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_kortilla_oikea_palautusarvo_(self):
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True
        )

    def test_syo_maukkaasti_kortilla_oikea_palautusarvo(self):
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True
        )

    # Jos kortilla on tarpeeksi rahaa lounaiden määrä kasvaa
    def test_korttimaksu_lounaiden_maara_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttimaksu_lounaiden_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Jos kortilla ei ole tarpeeksi rahaa saldo ei muutu
    def test_kortin_saldo_ei_mene_negatiiviseksi_edullinen(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    def test_kortin_saldo_ei_mene_negatiiviseksi_maukas(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    # Jos kortilla ei ole tarpeeksi rahaa myytyjen lounaiden määrä ei muutu
    def test_riittamaton_korttimaksu_lounaiden_maara_ei_muutu_edullinen(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_riittamaton_korttimaksu_lounaiden_maara_ei_muutu_maukas(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Jos kortilla ei ole tarpeeksi rahaa maksutapahtuma palautta false
    def test_syo_edullisesti_kortilla_oikea_palautusarvo_kun_raha_ei_riita(self):
        self.maksukortti = Maksukortti(100)

        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False
        )

    def test_syo_maukkaasti_kortilla_oikea_palautusarvo_kun_raha_ei_riita(self):
        self.maksukortti = Maksukortti(100)

        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False
        )

    # Kortille rahan lataaminen toimii oikein
    def test_lataa_rahaa_kortille_muuttaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_lataa_rahaa_kortille_muuttaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.00)

    def test_negatiivisen_summan_lataaminen_palauttaa_None(self):
        self.assertEqual(
            self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100), None
        )
