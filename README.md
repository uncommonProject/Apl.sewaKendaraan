# Sistem Rental Kendaraan

Tugas Besar Pemrograman Berorientasi Objek (INF2516) - Program Studi Informatika.

Aplikasi Python untuk menyewa mobil dan motor: pendaftaran pelanggan, proses sewa, struk, dan laporan pendapatan.

**Status:** Pertemuan 11 - Milestone Desain (tema, pembagian class, draft UML).

## Konsep PBO yang Direncanakan

- **Encapsulation**: atribut dengan awalan underscore, diakses lewat `@property` dan setter yang divalidasi
- **Inheritance**: `Mobil` dan `Motor` mewarisi `Kendaraan`
- **Polymorphism**: `hitung_biaya()` berbeda pada `Mobil` (asuransi 5%) dan `Motor` (diskon 10% untuk sewa 7 hari atau lebih)
- **Exception Handling dan Custom Exception**: `TarifTidakValidError`, `PelangganTidakTerdaftarError`, `KendaraanTidakTersediaError`, `DataLaporanKosongError`
- **Collection**: list (riwayat, data laporan) dan dictionary (pelanggan terdaftar, rekap per jenis)
- **Unit Test**: modul `unittest`

## Pembagian Class

| Anggota | Nama | NIM | Class |
|---|---|---|---|
| A | Imam Taufiq N | 60225055 | Laporan |
| B | Gulam Nuzul Kautsar | 60225127 | Penyewaan |
| C | Reyhan Mochamad Ikhbal | 60225098 | Pelanggan |
| D | Firgiawan Zhaliam | 60225081 | Kendaraan, Mobil, Motor |

## Dokumen

- [Desain dan UML Class Diagram](docs/UML_Class_Diagram.md)
- [Logbook Pertemuan 11](docs/logbook_pertemuan_11.md)

## Jadwal Milestone

| Pertemuan | Milestone | Status |
|---|---|---|
| 11 | Desain: daftar anggota, tema, draft UML | Dikerjakan |
| 12 | Progress 1: skeleton code tiap class | Menyusul |
| 13 | Progress 2: class berjalan, custom exception, unit test | Menyusul |
| 14 | Pengujian: laporan unit test | Menyusul |
| 15 | Final: source code, laporan PDF, logbook, video | Menyusul |
