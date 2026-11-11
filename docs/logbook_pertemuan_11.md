# Logbook Kelompok - Pertemuan 11

**Tema:** Sistem Rental Kendaraan
**Milestone:** Desain (Daftar Anggota + Tema + Draft UML Class)

| Anggota | Nama | NIM | Class yang dipegang |
|---|---|---|---|
| A | Imam Taufiq N | 60225055 | Laporan |
| B | Gulam Nuzul Kautsar | 60225127 | Penyewaan |
| C | Reyhan Mochamad Ikhbal | 60225098 | Pelanggan |
| D | Firgiawan Zhaliam | 60225081 | Kendaraan (Mobil, Motor) |

## Aktivitas Bersama

- Menentukan tema Sistem Rental Kendaraan (sewa mobil dan motor)
- Menyusun kebutuhan fungsional dan non-fungsional
- Membagi class sesuai aturan 1 anggota = 1 class utama
- Menggambar draft UML class diagram gabungan

## Logbook per Anggota

| Pertemuan | Anggota | Aktivitas | Output | Kendala dan solusi | Paraf Ketua |
|---|---|---|---|---|---|
| Pert. 11 | Imam Taufiq N | Mendesain class `Laporan`: atribut `_data`, method `tambah`, `jumlah_transaksi`, `cetak_struk`, `total_pendapatan`, `rekap_per_jenis`, dan exception `DataLaporanKosongError` | `docs/UML_Class_Diagram.md` | Bingung apakah `Laporan` menyimpan data sendiri atau mengambil dari `Penyewaan`. Solusi: `Laporan` menyimpan list `Penyewaan` yang sudah diproses (aggregation). | (ttd) |
| Pert. 11 | Gulam Nuzul Kautsar | Mendesain class `Penyewaan`: atribut `_kendaraan`, `_pelanggan`, `_hari`, `_selesai`, method `total_biaya` dan `proses`, serta exception `KendaraanTidakTersediaError` | `docs/UML_Class_Diagram.md` | Bingung batas tanggung jawab validasi antara `Penyewaan`, `Kendaraan`, dan `Pelanggan`. Solusi: `Penyewaan` mengecek status lalu memanggil method milik class lain. | (ttd) |
| Pert. 11 | Reyhan Mochamad Ikhbal | Mendesain class `Pelanggan`: atribut `_id_pelanggan`, `_nama`, `_riwayat`, `_terdaftar`, method `daftar`, `cari`, `tambah_riwayat`, `get_riwayat`, serta exception `PelangganTidakTerdaftarError` | `docs/UML_Class_Diagram.md` | Bingung cara menjamin ID pelanggan unik. Solusi: dictionary milik class (`_terdaftar`) dengan ID sebagai key. | (ttd) |
| Pert. 11 | Firgiawan Zhaliam | Mendesain class `Kendaraan` beserta turunan `Mobil` dan `Motor`: atribut, `hitung_biaya` (polymorphism), dan exception `TarifTidakValidError` | `docs/UML_Class_Diagram.md` | Bingung menentukan method yang di-override di `Mobil` dan `Motor`. Solusi: `hitung_biaya()` dibuat di class induk, lalu di-override di tiap turunan. | (ttd) |
