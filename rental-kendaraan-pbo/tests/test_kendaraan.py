import unittest
from kendaraan import Kendaraan, Mobil, Motor, TarifTidakValidError


class TestKendaraan(unittest.TestCase):
    def test_atribut_dan_status_awal(self):
        k = Kendaraan("G 1 A", "Generik", 100000)
        self.assertEqual(k.plat, "G 1 A")
        self.assertTrue(k.tersedia)

    def test_tarif_tidak_valid(self):
        with self.assertRaises(TarifTidakValidError):
            Kendaraan("G 1 A", "Generik", 0)
        with self.assertRaises(TarifTidakValidError):
            Kendaraan("G 1 A", "Generik", "murah")

    def test_setter_tarif(self):
        k = Kendaraan("G 1 A", "Generik", 100000)
        k.tarif_per_hari = 150000
        self.assertEqual(k.tarif_per_hari, 150000)
        with self.assertRaises(TarifTidakValidError):
            k.tarif_per_hari = -5

    def test_biaya_mobil_ada_asuransi(self):
        self.assertAlmostEqual(Mobil("G 1 A", "Avanza", 300000, 7).hitung_biaya(2), 630000)

    def test_biaya_motor_diskon_7_hari(self):
        m = Motor("G 2 B", "Beat", 100000, 110)
        self.assertAlmostEqual(m.hitung_biaya(3), 300000)
        self.assertAlmostEqual(m.hitung_biaya(7), 630000)

    def test_polymorphism(self):
        for k, jenis in [(Mobil("G 1 A", "A", 100000, 5), "Mobil"),
                         (Motor("G 2 B", "B", 100000, 110), "Motor")]:
            self.assertEqual(k.jenis(), jenis)
            self.assertIsInstance(k, Kendaraan)


if __name__ == "__main__":
    unittest.main()
