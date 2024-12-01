import csv
import os
from datetime import datetime

file_path_akun = "akun.csv"
file_path_stok = "stok.csv"
file_path_penjualan = "penjualan.csv"
file_path_pengeluaran = "pengeluaran.csv"
file_path_keuangan = "keuangan.csv"

# Fungsi untuk memastikan file CSV ada
def memastikan_csv_ada():
    if not os.path.exists(file_path_akun):
        with open(file_path_akun, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["role", "nama", "pin"])
            writer.writerow(["pemilik_toko", "saviya", "1234"])
            writer.writerow(["penjual", "satriyo", "1080"])
    if not os.path.exists(file_path_stok):
        with open(file_path_stok, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["nama_tanaman", "stok", "harga_beli", "harga_jual"])
    if not os.path.exists(file_path_penjualan):
        with open(file_path_penjualan, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["nama_tanaman", "jumlah", "total_harga", "tanggal", "waktu"])
    if not os.path.exists(file_path_pengeluaran):
        with open(file_path_pengeluaran, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["tanggal", "deskripsi", "jumlah"])
    if not os.path.exists(file_path_keuangan):
        with open(file_path_keuangan, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["tanggal", "keterangan", "jumlah", "saldo"])
            writer.writerow([datetime.now().strftime("%Y-%m-%d"), "Saldo Awal", "0", "0"])

# Fungsi untuk membaca data CSV
def baca_csv(file_path):
    data = []
    if os.path.exists(file_path):
        with open(file_path, mode="r") as file:
            baca = csv.DictReader(file)
            for row in baca:
                data.append(row)
    return data

# Fungsi untuk menulis data ke CSV
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Fungsi utama
def main():
    memastikan_csv_ada()
    akun = baca_csv(file_path_akun)
    os.system("cls")

    print("\n===========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊===========")
    print("=== SELAMAT DATANG DI DECPLANTS ===")
    print("====== SILAKAN LOGIN SEBAGAI: =====")
    print("===================================")
    print("======      1. Pemilik       ======")
    print("======      2. Penjual       ======")
    print("===========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊===========")

    try:
        role_pilihan = int(input("Silakan Pilih Opsi Antara 1/2: "))
        role = "pemilik_toko" if role_pilihan == 1 else "penjual" if role_pilihan == 2 else None

        if not role:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            main()

        nama = input("Silakan Masukkan Nama : ")
        pin = input("Silakan Masukkan Pin: ")

        for account in akun:
            if account["role"] == role and account["nama"] == nama and account["pin"] == pin:
                print(f"Login Berhasil! Selamat datang, {nama}.")
                os.system("cls")
                interface_pemilik() if role == "pemilik_toko" else interface_penjual()
                return
        
        print("Login Gagal! Nama pengguna atau kata sandi salah.")
        input("Tekan enter untuk kembali")
        os.system("cls")
        main()
    except ValueError:
        print("Masukkan pilihan yang valid!")