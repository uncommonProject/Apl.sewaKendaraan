"""Class Laporan (Anggota D)."""


class DataLaporanKosongError(Exception):
    """Dilempar jika laporan diminta saat belum ada transaksi."""


class Laporan:
    """Menyimpan seluruh transaksi dan membuat struk serta rekap."""

    def __init__(self):
        self._data = []  # list transaksi (objek Penyewaan)

    def tambah(self, penyewaan):
        self._data.append(penyewaan)

    def jumlah_transaksi(self):
        return len(self._data)

    def cetak_struk(self, penyewaan):
        garis = "=" * 36
        return "\n".join([
            garis,
            "STRUK RENTAL KENDARAAN",
            garis,
            f"Pelanggan : {penyewaan.pelanggan.nama}",
            f"Kendaraan : {penyewaan.kendaraan.merk} ({penyewaan.kendaraan.plat})",
            f"Jenis     : {penyewaan.kendaraan.jenis()}",
            f"Durasi    : {penyewaan.hari} hari",
            f"Total     : Rp{penyewaan.total_biaya():,.0f}",
            garis,
        ])

    def total_pendapatan(self):
        if not self._data:
            raise DataLaporanKosongError("Belum ada transaksi.")
        return sum(p.total_biaya() for p in self._data)

    def rekap_per_jenis(self):
        """Dictionary: jenis kendaraan -> total pendapatan."""
        if not self._data:
            raise DataLaporanKosongError("Belum ada transaksi.")
        rekap = {}
        for p in self._data:
            jenis = p.kendaraan.jenis()
            rekap[jenis] = rekap.get(jenis, 0) + p.total_biaya()
        return rekap
