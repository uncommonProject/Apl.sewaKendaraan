import unittest
from kendaraan import Mobil
from pelanggan import Pelanggan, PelangganTidakTerdaftarError
from penyewaan import Penyewaan, KendaraanTidakTersediaError


class TestPenyewaan(unittest.TestCase):
    def setUp(self):
        Pelanggan.reset()
        self.mobil = Mobil("G 1 A", "Avanza", 300000, 7)
        self.budi = Pelanggan("P1", "Budi")
        self.budi.daftar()

    def test_total_biaya(self):
        self.assertAlmostEqual(Penyewaan(self.mobil, self.budi, 2).total_biaya(), 630000)

    def test_proses_berhasil(self):
        p = Penyewaan(self.mobil, self.budi, 2)
        p.proses()
        self.assertFalse(self.mobil.tersedia)
        self.assertTrue(p.selesai)
        self.assertEqual(self.budi.get_riwayat(), [p])

    def test_kendaraan_tidak_tersedia(self):
        Penyewaan(self.mobil, self.budi, 1).proses()
        with self.assertRaises(KendaraanTidakTersediaError):
            Penyewaan(self.mobil, self.budi, 1).proses()

    def test_pelanggan_belum_terdaftar(self):
        Pelanggan.reset()
        with self.assertRaises(PelangganTidakTerdaftarError):
            Penyewaan(self.mobil, self.budi, 1).proses()

    def test_durasi_tidak_valid(self):
        with self.assertRaises(ValueError):
            Penyewaan(self.mobil, self.budi, 0)


if __name__ == "__main__":
    unittest.main()
