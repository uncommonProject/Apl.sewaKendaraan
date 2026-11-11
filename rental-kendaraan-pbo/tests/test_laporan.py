import unittest
from kendaraan import Mobil, Motor
from pelanggan import Pelanggan
from penyewaan import Penyewaan
from laporan import Laporan, DataLaporanKosongError


class TestLaporan(unittest.TestCase):
    def setUp(self):
        Pelanggan.reset()
        self.budi = Pelanggan("P1", "Budi")
        self.budi.daftar()
        self.laporan = Laporan()

    def test_laporan_kosong(self):
        with self.assertRaises(DataLaporanKosongError):
            self.laporan.total_pendapatan()
        with self.assertRaises(DataLaporanKosongError):
            self.laporan.rekap_per_jenis()

    def test_total_dan_rekap(self):
        self.laporan.tambah(Penyewaan(Mobil("G 1 A", "Avanza", 300000, 7), self.budi, 2))
        self.laporan.tambah(Penyewaan(Motor("G 2 B", "Beat", 100000, 110), self.budi, 3))
        self.assertEqual(self.laporan.jumlah_transaksi(), 2)
        self.assertAlmostEqual(self.laporan.total_pendapatan(), 930000)
        rekap = self.laporan.rekap_per_jenis()
        self.assertAlmostEqual(rekap["Mobil"], 630000)
        self.assertAlmostEqual(rekap["Motor"], 300000)

    def test_cetak_struk(self):
        p = Penyewaan(Mobil("G 1 A", "Avanza", 300000, 7), self.budi, 2)
        struk = self.laporan.cetak_struk(p)
        self.assertIn("Budi", struk)
        self.assertIn("Avanza", struk)
        self.assertIn("630,000", struk)


if __name__ == "__main__":
    unittest.main()
