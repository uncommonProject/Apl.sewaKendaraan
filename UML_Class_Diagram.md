# Desain Sistem Rental Kendaraan

Pertemuan 11 - Milestone Desain (Tugas Besar PBO, INF2516)

**Tema:** Sistem Rental Kendaraan (sewa mobil dan motor)

## 1. Kebutuhan Sistem

### Kebutuhan fungsional

| Kode | Kebutuhan | Class pemegang |
|---|---|---|
| F-01 | Melihat daftar kendaraan beserta status (Tersedia/Disewa) | `Kendaraan` |
| F-02 | Mendaftarkan pelanggan baru (ID unik, ID dan nama tidak boleh kosong) | `Pelanggan` |
| F-03 | Memproses sewa: cek pelanggan terdaftar, cek kendaraan tersedia, durasi bilangan bulat > 0 | `Penyewaan` |
| F-04 | Menghitung biaya sesuai jenis: Mobil + asuransi 5%, Motor diskon 10% jika sewa 7 hari atau lebih | `Mobil`, `Motor` |
| F-05 | Mencetak struk transaksi | `Laporan` |
| F-06 | Mengembalikan kendaraan yang disewa | `Kendaraan` |
| F-07 | Menampilkan jumlah transaksi, total pendapatan, dan rekap per jenis | `Laporan` |
| F-08 | Menyimpan riwayat sewa tiap pelanggan | `Pelanggan` |

### Kebutuhan non-fungsional

- Satu anggota bertanggung jawab atas satu class utama.
- Dua antarmuka: konsol dan web (Streamlit).
- Input tidak valid ditangani dengan custom exception.
- Setiap class diuji dengan `unittest`.

## 2. Pembagian Class

| Anggota | Nama | Class |
|---|---|---|
| A | Imam Taufiq N | Laporan |
| B | Gulam Nuzul Kautsar | Penyewaan |
| C | Reyhan Mochamad Ikhbal | Pelanggan |
| D | Firgiawan Zhaliam | Kendaraan, Mobil, Motor |

`Mobil` dan `Motor` adalah turunan `Kendaraan` (satu hierarki inheritance), sehingga dihitung sebagai satu kesatuan class utama.

## 3. Class Diagram

```mermaid
classDiagram
    class Kendaraan {
        #str _plat
        #str _merk
        #float _tarif_per_hari
        #bool _tersedia
        +plat() str
        +merk() str
        +tarif_per_hari() float
        +tersedia() bool
        +jenis() str
        +hitung_biaya(hari) float
        +info() str
    }
    class Mobil {
        #int _kapasitas
        +kapasitas() int
        +jenis() str
        +hitung_biaya(hari) float
    }
    class Motor {
        #int _cc
        +cc() int
        +jenis() str
        +hitung_biaya(hari) float
    }
    class Pelanggan {
        #str _id_pelanggan
        #str _nama
        #list _riwayat
        #dict _terdaftar$
        +id_pelanggan() str
        +nama() str
        +daftar() void
        +cari(id_pelanggan)$ Pelanggan
        +daftar_semua()$ list
        +reset()$ void
        +tambah_riwayat(penyewaan) void
        +get_riwayat() list
    }
    class Penyewaan {
        #Kendaraan _kendaraan
        #Pelanggan _pelanggan
        #int _hari
        #bool _selesai
        +total_biaya() float
        +proses() void
    }
    class Laporan {
        #list _data
        +tambah(penyewaan) void
        +jumlah_transaksi() int
        +cetak_struk(penyewaan) str
        +total_pendapatan() float
        +rekap_per_jenis() dict
    }
    class TarifTidakValidError {
        <<exception>>
    }
    class PelangganTidakTerdaftarError {
        <<exception>>
    }
    class KendaraanTidakTersediaError {
        <<exception>>
    }
    class DataLaporanKosongError {
        <<exception>>
    }

    Kendaraan <|-- Mobil
    Kendaraan <|-- Motor
    Penyewaan "*" --> "1" Kendaraan : menyewa
    Penyewaan "*" --> "1" Pelanggan : disewa oleh
    Pelanggan "1" o-- "*" Penyewaan : riwayat
    Laporan "1" o-- "*" Penyewaan : _data
    Kendaraan ..> TarifTidakValidError : raise
    Pelanggan ..> PelangganTidakTerdaftarError : raise
    Penyewaan ..> KendaraanTidakTersediaError : raise
    Laporan ..> DataLaporanKosongError : raise
```

### Keterangan notasi

- `#` = protected (konvensi satu underscore), `+` = public, `$` = milik class (static).
- `<|--` inheritance, `-->` association, `o--` aggregation, `..>` dependensi exception.
