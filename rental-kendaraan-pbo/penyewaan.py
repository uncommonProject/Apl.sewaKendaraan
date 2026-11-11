"""Class Penyewaan (Anggota C)."""

from pelanggan import Pelanggan


class KendaraanTidakTersediaError(Exception):
    """Dilempar jika kendaraan sedang disewa."""


class Penyewaan:
    """Satu transaksi sewa antara Pelanggan dan Kendaraan."""

    def __init__(self, kendaraan, pelanggan, hari):
        if not isinstance(hari, int) or hari <= 0:
            raise ValueError("Durasi sewa harus berupa bilangan bulat lebih dari 0.")
        self._kendaraan = kendaraan
        self._pelanggan = pelanggan
        self._hari = hari
        self._selesai = False

    @property
    def kendaraan(self):
        return self._kendaraan

    @property
    def pelanggan(self):
        return self._pelanggan

    @property
    def hari(self):
        return self._hari

    @property
    def selesai(self):
        return self._selesai

    def total_biaya(self):
        # Polymorphism: rumus biaya ditentukan oleh jenis kendaraan
        return self._kendaraan.hitung_biaya(self._hari)

    def proses(self):
        """Memproses sewa: cek pelanggan, cek kendaraan, ubah status, catat riwayat."""
        Pelanggan.cari(self._pelanggan.id_pelanggan)
        if not self._kendaraan.tersedia:
            raise KendaraanTidakTersediaError(
                f"{self._kendaraan.merk} ({self._kendaraan.plat}) sedang disewa.")
        self._kendaraan.tersedia = False
        self._pelanggan.tambah_riwayat(self)
        self._selesai = True
