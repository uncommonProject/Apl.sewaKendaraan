"""Class Kendaraan beserta subclass Mobil dan Motor (Anggota A)."""


class TarifTidakValidError(Exception):
    """Dilempar jika tarif per hari bukan angka positif."""


class Kendaraan:
    """Kelas dasar untuk semua kendaraan yang bisa disewa."""

    def __init__(self, plat, merk, tarif_per_hari):
        self._plat = plat
        self._merk = merk
        self._tersedia = True
        self.tarif_per_hari = tarif_per_hari  # lewat setter agar divalidasi

    @property
    def plat(self):
        return self._plat

    @property
    def merk(self):
        return self._merk

    @property
    def tarif_per_hari(self):
        return self._tarif_per_hari

    @tarif_per_hari.setter
    def tarif_per_hari(self, nilai):
        if isinstance(nilai, bool) or not isinstance(nilai, (int, float)) or nilai <= 0:
            raise TarifTidakValidError("Tarif per hari harus berupa angka lebih dari 0.")
        self._tarif_per_hari = nilai

    @property
    def tersedia(self):
        return self._tersedia

    @tersedia.setter
    def tersedia(self, nilai):
        self._tersedia = bool(nilai)

    def jenis(self):
        return "Kendaraan"

    def hitung_biaya(self, hari):
        """Biaya dasar: tarif x hari. Di-override oleh subclass."""
        return self._tarif_per_hari * hari

    def info(self):
        status = "Tersedia" if self._tersedia else "Disewa"
        return (f"[{self.jenis()}] {self._merk} ({self._plat}) - "
                f"Rp{self._tarif_per_hari:,.0f}/hari - {status}")


class Mobil(Kendaraan):
    """Mobil: biaya sewa ditambah asuransi tetap 5%."""

    def __init__(self, plat, merk, tarif_per_hari, kapasitas):
        super().__init__(plat, merk, tarif_per_hari)
        self._kapasitas = kapasitas

    @property
    def kapasitas(self):
        return self._kapasitas

    def jenis(self):
        return "Mobil"

    def hitung_biaya(self, hari):
        return round(super().hitung_biaya(hari) * 1.05, 2)


class Motor(Kendaraan):
    """Motor: diskon 10% jika sewa 7 hari atau lebih."""

    def __init__(self, plat, merk, tarif_per_hari, cc):
        super().__init__(plat, merk, tarif_per_hari)
        self._cc = cc

    @property
    def cc(self):
        return self._cc

    def jenis(self):
        return "Motor"

    def hitung_biaya(self, hari):
        biaya = super().hitung_biaya(hari)
        if hari >= 7:
            biaya *= 0.9
        return round(biaya, 2)
