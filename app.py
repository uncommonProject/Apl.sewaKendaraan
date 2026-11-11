"""Sistem Rental Kendaraan - Tugas Besar PBO (INF2516).

Satu file berisi seluruh class dan tampilan Streamlit.
Menjalankan: streamlit run app.py
"""

import streamlit as st

# ============================================================
# Anggota A - Kendaraan, Mobil, Motor
# ============================================================

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


# ============================================================
# Anggota B - Pelanggan
# ============================================================

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


# ============================================================
# Anggota C - Penyewaan
# ============================================================

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


# ============================================================
# Anggota D - Laporan
# ============================================================

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


# ============================================================
# Data awal dan tampilan Streamlit
# ============================================================

def data_awal():
    return [
        Mobil("G 1234 AB", "Toyota Avanza", 300000, 7),
        Mobil("G 5678 CD", "Honda Brio", 250000, 5),
        Motor("G 1111 EF", "Honda Beat", 80000, 110),
        Motor("G 2222 GH", "Yamaha NMAX", 120000, 155),
    ]


ERRORS = (PelangganTidakTerdaftarError, KendaraanTidakTersediaError,
          TarifTidakValidError, DataLaporanKosongError, ValueError)


def init_state():
    if "kendaraan" not in st.session_state:
        Pelanggan.reset()
        st.session_state.kendaraan = data_awal()
        st.session_state.laporan = Laporan()
        st.session_state.struk = None
        st.session_state.pesan = None


def pesan(jenis, teks):
    """Simpan pesan lalu muat ulang halaman agar semua tab ikut diperbarui."""
    st.session_state.pesan = (jenis, teks)
    st.rerun()


def tab_kendaraan():
    daftar = st.session_state.kendaraan
    st.dataframe(
        [{"Jenis": k.jenis(), "Merek": k.merk, "Plat": k.plat,
          "Tarif/hari": f"Rp{k.tarif_per_hari:,.0f}",
          "Status": "Tersedia" if k.tersedia else "Disewa"} for k in daftar],
        use_container_width=True, hide_index=True)

    with st.expander("Tambah kendaraan"):
        with st.form("form_kendaraan", clear_on_submit=True):
            jenis = st.radio("Jenis", ["Mobil", "Motor"], horizontal=True)
            plat = st.text_input("Plat nomor")
            merk = st.text_input("Merek")
            tarif = st.number_input("Tarif per hari (Rp)", value=0, step=10000)
            tambahan = st.number_input("Kapasitas kursi (Mobil) / CC (Motor)",
                                       min_value=1, value=5)
            if st.form_submit_button("Simpan"):
                try:
                    if not plat.strip() or not merk.strip():
                        raise ValueError("Plat dan merek tidak boleh kosong.")
                    kelas = Mobil if jenis == "Mobil" else Motor
                    daftar.append(kelas(plat.strip(), merk.strip(), tarif, tambahan))
                except ERRORS as e:
                    st.error(str(e))
                else:
                    pesan("success", f"{jenis} {merk} berhasil ditambahkan.")


def tab_pelanggan():
    with st.form("form_pelanggan", clear_on_submit=True):
        id_p = st.text_input("ID pelanggan")
        nama = st.text_input("Nama pelanggan")
        if st.form_submit_button("Daftarkan"):
            try:
                Pelanggan(id_p, nama).daftar()
            except ERRORS as e:
                st.error(str(e))
            else:
                pesan("success", f"Pelanggan {nama} berhasil didaftarkan.")

    semua = Pelanggan.daftar_semua()
    if semua:
        st.dataframe(
            [{"ID": p.id_pelanggan, "Nama": p.nama,
              "Jumlah sewa": len(p.get_riwayat())} for p in semua],
            use_container_width=True, hide_index=True)
    else:
        st.info("Belum ada pelanggan terdaftar.")


def tab_sewa():
    daftar = st.session_state.kendaraan
    with st.form("form_sewa"):
        id_p = st.text_input("ID pelanggan")
        indeks = st.selectbox("Kendaraan", range(len(daftar)),
                              format_func=lambda i: daftar[i].info())
        hari = st.number_input("Lama sewa (hari)", min_value=1, value=1, step=1)
        kirim = st.form_submit_button("Proses sewa")

    if kirim:
        try:
            pelanggan = Pelanggan.cari(id_p)
            transaksi = Penyewaan(daftar[indeks], pelanggan, int(hari))
            transaksi.proses()
            st.session_state.laporan.tambah(transaksi)
            st.session_state.struk = st.session_state.laporan.cetak_struk(transaksi)
        except ERRORS as e:
            st.error(str(e))
        else:
            pesan("success", "Sewa berhasil diproses.")

    if st.session_state.struk:
        st.code(st.session_state.struk, language=None)

    st.subheader("Kembalikan kendaraan")
    disewa = [k for k in daftar if not k.tersedia]
    if disewa:
        pilih = st.selectbox("Kendaraan yang disewa", range(len(disewa)),
                             format_func=lambda i: disewa[i].info())
        if st.button("Kembalikan"):
            disewa[pilih].tersedia = True
            pesan("success", "Kendaraan sudah dikembalikan.")
    else:
        st.caption("Tidak ada kendaraan yang sedang disewa.")


def tab_laporan():
    laporan = st.session_state.laporan
    try:
        total = laporan.total_pendapatan()
        rekap = laporan.rekap_per_jenis()
    except DataLaporanKosongError as e:
        st.info(str(e))
        return
    kiri, kanan = st.columns(2)
    kiri.metric("Jumlah transaksi", laporan.jumlah_transaksi())
    kanan.metric("Total pendapatan", f"Rp{total:,.0f}")
    st.bar_chart(rekap)


def main():
    st.set_page_config(page_title="Rental Kendaraan", page_icon="🚗")
    st.title("🚗 Sistem Rental Kendaraan")
    init_state()

    if st.session_state.pesan:
        jenis, teks = st.session_state.pesan
        st.session_state.pesan = None
        (st.success if jenis == "success" else st.error)(teks)

    t1, t2, t3, t4 = st.tabs(["Kendaraan", "Pelanggan", "Sewa", "Laporan"])
    with t1:
        tab_kendaraan()
    with t2:
        tab_pelanggan()
    with t3:
        tab_sewa()
    with t4:
        tab_laporan()


main()
