import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_on_oikea(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 30.0)

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(5000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_True_jos_saldo_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_ota_rahaa_palauttaa_True_jos_saldo_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)
