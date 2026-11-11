"""Program utama Sistem Rental Kendaraan (integrasi semua class)."""

from kendaraan import Mobil, Motor, TarifTidakValidError
from pelanggan import Pelanggan, PelangganTidakTerdaftarError
from penyewaan import Penyewaan, KendaraanTidakTersediaError
from laporan import Laporan, DataLaporanKosongError


def data_awal():
    return [
        Mobil("G 1234 AB", "Toyota Avanza", 300000, 7),
        Mobil("G 5678 CD", "Honda Brio", 250000, 5),
        Motor("G 1111 EF", "Honda Beat", 80000, 110),
        Motor("G 2222 GH", "Yamaha NMAX", 120000, 155),
    ]


def baca_angka(pesan):
    try:
        return int(input(pesan))
    except ValueError:
        raise ValueError("Input harus berupa angka.")


def tampil_kendaraan(daftar):
    for nomor, k in enumerate(daftar, 1):
        print(f"{nomor}. {k.info()}")


def pilih_kendaraan(daftar):
    nomor = baca_angka("Nomor kendaraan: ")
    if not 1 <= nomor <= len(daftar):
        raise ValueError("Nomor kendaraan tidak ada.")
    return daftar[nomor - 1]


def daftar_pelanggan():
    id_p = input("ID pelanggan: ")
    nama = input("Nama pelanggan: ")
    Pelanggan(id_p, nama).daftar()
    print("Pelanggan berhasil didaftarkan.")


def sewa(daftar, laporan):
    pelanggan = Pelanggan.cari(input("ID pelanggan: "))
    tampil_kendaraan(daftar)
    kendaraan = pilih_kendaraan(daftar)
    hari = baca_angka("Lama sewa (hari): ")
    transaksi = Penyewaan(kendaraan, pelanggan, hari)
    transaksi.proses()
    laporan.tambah(transaksi)
    print(laporan.cetak_struk(transaksi))


def kembalikan(daftar):
    tampil_kendaraan(daftar)
    pilih_kendaraan(daftar).tersedia = True
    print("Kendaraan sudah dikembalikan.")


def tampil_laporan(laporan):
    print(f"Jumlah transaksi : {laporan.jumlah_transaksi()}")
    print(f"Total pendapatan : Rp{laporan.total_pendapatan():,.0f}")
    for jenis, total in laporan.rekap_per_jenis().items():
        print(f"  {jenis}: Rp{total:,.0f}")


def main():
    daftar = data_awal()
    laporan = Laporan()
    menu = ("\n=== RENTAL KENDARAAN ===\n"
            "1. Lihat kendaraan\n2. Daftar pelanggan\n3. Sewa kendaraan\n"
            "4. Kembalikan kendaraan\n5. Laporan\n0. Keluar")
    while True:
        print(menu)
        try:
            pilihan = input("Pilih menu: ").strip()
            if pilihan == "1":
                tampil_kendaraan(daftar)
            elif pilihan == "2":
                daftar_pelanggan()
            elif pilihan == "3":
                sewa(daftar, laporan)
            elif pilihan == "4":
                kembalikan(daftar)
            elif pilihan == "5":
                tampil_laporan(laporan)
            elif pilihan == "0":
                print("Terima kasih.")
                break
            else:
                print("Menu tidak dikenal.")
        except (PelangganTidakTerdaftarError, KendaraanTidakTersediaError,
                TarifTidakValidError, DataLaporanKosongError, ValueError) as e:
            print(f"[GAGAL] {e}")
        except EOFError:
            break


if __name__ == "__main__":
    main()
