"""Tampilan Streamlit untuk Sistem Rental Kendaraan.

Jalankan dengan: streamlit run app_streamlit.py
"""

import streamlit as st

from kendaraan import TarifTidakValidError
from pelanggan import Pelanggan, PelangganTidakTerdaftarError
from penyewaan import Penyewaan, KendaraanTidakTersediaError
from laporan import Laporan, DataLaporanKosongError
from main import data_awal

st.set_page_config(page_title="Rental Kendaraan", page_icon="🚗")

# Data disimpan di session_state agar tidak hilang saat halaman dimuat ulang
if "kendaraan" not in st.session_state:
    Pelanggan.reset()
    st.session_state.kendaraan = data_awal()
    st.session_state.laporan = Laporan()
    st.session_state.struk = None

daftar = st.session_state.kendaraan
laporan = st.session_state.laporan

st.title("🚗 Sistem Rental Kendaraan")
tab1, tab2, tab3, tab4 = st.tabs(["Kendaraan", "Pelanggan", "Sewa", "Laporan"])

# ---------- Tab Kendaraan ----------
with tab1:
    st.subheader("Daftar Kendaraan")
    st.dataframe(
        [{"Jenis": k.jenis(), "Merk": k.merk, "Plat": k.plat,
          "Tarif/hari (Rp)": k.tarif_per_hari,
          "Status": "Tersedia" if k.tersedia else "Disewa"} for k in daftar],
        use_container_width=True, hide_index=True)

    disewa = [k for k in daftar if not k.tersedia]
    if disewa:
        pilih = st.selectbox("Kembalikan kendaraan", disewa,
                             format_func=lambda k: f"{k.merk} ({k.plat})")
        if st.button("Kembalikan"):
            pilih.tersedia = True
            st.rerun()

# ---------- Tab Pelanggan ----------
with tab2:
    st.subheader("Daftar Pelanggan Baru")
    id_p = st.text_input("ID pelanggan", key="id_baru")
    nama = st.text_input("Nama pelanggan", key="nama_baru")
    if st.button("Daftarkan"):
        try:
            Pelanggan(id_p, nama).daftar()
            st.success("Pelanggan berhasil didaftarkan.")
        except ValueError as e:
            st.error(str(e))

    st.subheader("Pelanggan Terdaftar")
    st.dataframe(
        [{"ID": p.id_pelanggan, "Nama": p.nama,
          "Jumlah sewa": len(p.get_riwayat())} for p in Pelanggan.daftar_semua()],
        use_container_width=True, hide_index=True)

# ---------- Tab Sewa ----------
with tab3:
    st.subheader("Sewa Kendaraan")
    id_sewa = st.text_input("ID pelanggan", key="id_sewa")
    kendaraan = st.selectbox("Kendaraan", daftar,
                             format_func=lambda k: k.info())
    hari = st.number_input("Lama sewa (hari)", min_value=1, value=1, step=1)
    if st.button("Proses Sewa"):
        try:
            pelanggan = Pelanggan.cari(id_sewa)
            transaksi = Penyewaan(kendaraan, pelanggan, int(hari))
            transaksi.proses()
            laporan.tambah(transaksi)
            st.session_state.struk = laporan.cetak_struk(transaksi)
            st.rerun()
        except (PelangganTidakTerdaftarError, KendaraanTidakTersediaError,
                TarifTidakValidError, ValueError) as e:
            st.session_state.struk = None
            st.error(str(e))

    if st.session_state.struk:
        st.success("Sewa berhasil diproses.")
        st.code(st.session_state.struk, language=None)

# ---------- Tab Laporan ----------
with tab4:
    st.subheader("Laporan Pendapatan")
    try:
        st.metric("Jumlah transaksi", laporan.jumlah_transaksi())
        st.metric("Total pendapatan", f"Rp{laporan.total_pendapatan():,.0f}")
        st.bar_chart(laporan.rekap_per_jenis())
    except DataLaporanKosongError as e:
        st.info(str(e))
