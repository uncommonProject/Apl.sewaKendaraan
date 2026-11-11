"""Class Pelanggan (Anggota B)."""


class PelangganTidakTerdaftarError(Exception):
    """Dilempar jika ID pelanggan belum terdaftar."""


class Pelanggan:
    """Data pelanggan dan riwayat sewanya."""

    _terdaftar = {}  # dictionary: id_pelanggan -> objek Pelanggan

    def __init__(self, id_pelanggan, nama):
        if not str(id_pelanggan).strip() or not str(nama).strip():
            raise ValueError("ID dan nama pelanggan tidak boleh kosong.")
        self._id_pelanggan = str(id_pelanggan).strip()
        self._nama = str(nama).strip()
        self._riwayat = []

    @property
    def id_pelanggan(self):
        return self._id_pelanggan

    @property
    def nama(self):
        return self._nama

    def daftar(self):
        """Mendaftarkan pelanggan ke sistem."""
        if self._id_pelanggan in Pelanggan._terdaftar:
            raise ValueError(f"ID {self._id_pelanggan} sudah terdaftar.")
        Pelanggan._terdaftar[self._id_pelanggan] = self

    @classmethod
    def cari(cls, id_pelanggan):
        """Mengambil pelanggan terdaftar, atau melempar exception."""
        try:
            return cls._terdaftar[str(id_pelanggan).strip()]
        except KeyError:
            raise PelangganTidakTerdaftarError(
                f"Pelanggan dengan ID {id_pelanggan} belum terdaftar.")

    @classmethod
    def daftar_semua(cls):
        """Mengembalikan list semua pelanggan terdaftar."""
        return list(cls._terdaftar.values())

    @classmethod
    def reset(cls):
        """Mengosongkan data pelanggan (dipakai saat pengujian)."""
        cls._terdaftar = {}

    def tambah_riwayat(self, penyewaan):
        self._riwayat.append(penyewaan)

    def get_riwayat(self):
        return list(self._riwayat)
