# Sistem Rental Kendaraan

Tugas Besar Pemrograman Berorientasi Objek (INF2516) - Program Studi Informatika.

Aplikasi Python untuk menyewa mobil dan motor: pendaftaran pelanggan, proses sewa, struk, dan laporan pendapatan. Tersedia dalam dua tampilan: konsol dan Streamlit.

## Konsep PBO yang Diterapkan

- **Encapsulation**: atribut private dengan `@property` dan setter yang divalidasi
- **Inheritance**: `Mobil` dan `Motor` mewarisi `Kendaraan`
- **Polymorphism**: `hitung_biaya()` berbeda pada `Mobil` (asuransi 5%) dan `Motor` (diskon 10% untuk sewa 7 hari atau lebih)
- **Exception Handling dan Custom Exception**: `TarifTidakValidError`, `PelangganTidakTerdaftarError`, `KendaraanTidakTersediaError`, `DataLaporanKosongError`
- **Collection**: list (riwayat, data laporan) dan dictionary (pelanggan terdaftar, rekap per jenis)
- **Unit Test**: modul `unittest`

## Pembagian Class

| Anggota | Class | File |
|---|---|---|
| A | Kendaraan, Mobil, Motor | `kendaraan.py` |
| B | Pelanggan | `pelanggan.py` |
| C | Penyewaan | `penyewaan.py` |
| D | Laporan | `laporan.py` |
| Bersama | Integrasi | `main.py`, `app_streamlit.py` |

## Struktur Folder

```
.
├── kendaraan.py
├── pelanggan.py
├── penyewaan.py
├── laporan.py
├── main.py              # versi konsol
├── app_streamlit.py     # versi Streamlit
├── requirements.txt
└── tests/
    ├── test_kendaraan.py
    ├── test_pelanggan.py
    ├── test_penyewaan.py
    └── test_laporan.py
```

## Cara Menjalankan

Versi konsol (hanya butuh Python 3):

```
python main.py
```

Versi Streamlit:

```
pip install -r requirements.txt
streamlit run app_streamlit.py
```

## Menjalankan Unit Test

```
python -m unittest discover -s tests -t . -v
```

## Anggota Kelompok

| Anggota | Nama | NIM |
|---|---|---|
| A | | |
| B | | |
| C | | |
| D | | |
