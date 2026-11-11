import unittest
from pelanggan import Pelanggan, PelangganTidakTerdaftarError


class TestPelanggan(unittest.TestCase):
    def setUp(self):
        Pelanggan.reset()

    def test_daftar_dan_cari(self):
        p = Pelanggan("P1", "Budi")
        p.daftar()
        self.assertIs(Pelanggan.cari("P1"), p)

    def test_cari_tidak_terdaftar(self):
        with self.assertRaises(PelangganTidakTerdaftarError):
            Pelanggan.cari("XXX")

    def test_id_ganda_ditolak(self):
        Pelanggan("P1", "Budi").daftar()
        with self.assertRaises(ValueError):
            Pelanggan("P1", "Siti").daftar()

    def test_data_kosong_ditolak(self):
        with self.assertRaises(ValueError):
            Pelanggan("P1", "  ")

    def test_daftar_semua(self):
        self.assertEqual(Pelanggan.daftar_semua(), [])
        p = Pelanggan("P1", "Budi")
        p.daftar()
        self.assertEqual(Pelanggan.daftar_semua(), [p])

    def test_riwayat(self):
        p = Pelanggan("P1", "Budi")
        self.assertEqual(p.get_riwayat(), [])
        p.tambah_riwayat("transaksi-1")
        self.assertEqual(p.get_riwayat(), ["transaksi-1"])


if __name__ == "__main__":
    unittest.main()
