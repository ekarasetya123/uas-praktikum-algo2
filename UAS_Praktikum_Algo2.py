import os

nama_file = "data_gaji.txt"

data_karyawan = []


def hitung_gaji(golongan, status):
    if golongan == "A":
        gaji_pokok = 200000
    else:
        gaji_pokok = 350000

    # Tunjangan
    if golongan == "A" and status == "Nikah":
        tunjangan = 50000
    elif golongan == "A" and status == "Belum":
        tunjangan = 25000
    elif golongan == "B" and status == "Nikah":
        tunjangan = 75000
    else:
        tunjangan = 60000

    if gaji_pokok <= 300000:
        prosentase = 0.05
    else:
        prosentase = 0.10

    potongan = (gaji_pokok + tunjangan) * prosentase

    gaji_bersih = gaji_pokok + tunjangan - potongan

    return gaji_pokok, tunjangan, potongan, gaji_bersih


def input_data():
    nama = input("Nama Karyawan   : ")
    golongan = input("Golongan (A/B) : ").upper()
    status = input("Status (Nikah/Belum) : ").capitalize()

    gaji_pokok, tunjangan, potongan, gaji_bersih = hitung_gaji(golongan, status)

    karyawan = {
        "nama": nama,
        "golongan": golongan,
        "status": status,
        "gaji_pokok": gaji_pokok,
        "tunjangan": tunjangan,
        "potongan": potongan,
        "gaji_bersih": gaji_bersih
    }

    data_karyawan.append(karyawan)

    print("\n=== Hasil Hitung Gaji ===")
    print("Nama Karyawan  :", nama)
    print("Golongan       :", golongan)
    print("Status         :", status)
    print("Gaji Pokok     : Rp.", gaji_pokok)
    print("Tunjangan      : Rp.", tunjangan)
    print("Potongan Iuran : Rp.", potongan)
    print("Gaji Bersih    : Rp.", gaji_bersih)
    print("=========================\n")

    simpan_ke_file(karyawan)


def simpan_ke_file(karyawan):
    file = open(nama_file, "a")
    baris = f"{karyawan['nama']},{karyawan['golongan']},{karyawan['status']},{karyawan['gaji_pokok']},{karyawan['tunjangan']},{karyawan['potongan']},{karyawan['gaji_bersih']}\n"
    file.write(baris)
    file.close()
    print("Data berhasil disimpan ke file.\n")


def tampilkan_data():
    if not os.path.exists(nama_file):
        print("Belum ada data tersimpan.\n")
        return

    file = open(nama_file, "r")
    baris_semua = file.readlines()
    file.close()

    if len(baris_semua) == 0:
        print("Belum ada data tersimpan.\n")
        return

    print("\n=== Data Gaji Karyawan ===")
    nomor = 1
    for baris in baris_semua:
        baris = baris.strip()
        kolom = baris.split(",")
        print(f"{nomor}. Nama: {kolom[0]} | Golongan: {kolom[1]} | Status: {kolom[2]} | Gaji Pokok: Rp.{kolom[3]} | Tunjangan: Rp.{kolom[4]} | Potongan: Rp.{kolom[5]} | Gaji Bersih: Rp.{kolom[6]}")
        nomor += 1
    print("===========================\n")


def hapus_data():
    if not os.path.exists(nama_file):
        print("Belum ada data tersimpan.\n")
        return

    file = open(nama_file, "r")
    baris_semua = file.readlines()
    file.close()

    if len(baris_semua) == 0:
        print("Belum ada data tersimpan.\n")
        return

    tampilkan_data()

    nomor_hapus = int(input("Masukkan nomor data yang mau dihapus: "))

    if nomor_hapus < 1 or nomor_hapus > len(baris_semua):
        print("Nomor tidak ditemukan.\n")
        return

    del baris_semua[nomor_hapus - 1]

    file = open(nama_file, "w")
    for baris in baris_semua:
        file.write(baris)
    file.close()

    print("Data berhasil dihapus.\n")


def main():
    while True:
        print("===== MENU APLIKASI PENGHITUNG GAJI =====")
        print("1. Input Data Gaji Karyawan")
        print("2. Tampilkan Data Gaji")
        print("3. Hapus Data Gaji")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            input_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak ada, coba lagi.\n")

main()