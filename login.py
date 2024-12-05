import csv
import os
from datetime import datetime
import pandas as pd
from tabulate import tabulate

file_path_akun = "akun.csv"
file_path_stok = "stok.csv"
file_path_penjualan = "penjualan.csv"
file_path_pengeluaran = "pengeluaran.csv"
file_path_keuangan = "keuangan.csv"

# Fungsi untuk membaca data CSV
def baca_csv(file_path):
    data = []
    if os.path.exists(file_path):
        with open(file_path, mode="r") as file:
            baca = csv.DictReader(file)
            for row in baca:
                data.append(row)
    return data

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

# Fungsi untuk menulis data ke CSV
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Fungsi utama
def main():
    os.system("cls")
    memastikan_csv_ada()
    akun = baca_csv(file_path_akun)
    print("\n===========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊===========")
    print("=== SELAMAT DATANG DI DECPLANTS ===")
    print("====== SILAKAN LOGIN SEBAGAI: =====")
    print("===========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊===========")

    menu_utama= [
        ["1", "Pemilik"],
        ["2", "Penjual"],
        ["3", "Keluar Aplikasi"]
    ]

    print(tabulate(menu_utama, headers=["No", "Menu"], tablefmt="double_grid"))

    try:
        role_pilihan = int(input("Silakan Pilih Opsi Antara 1/2/3: "))

        if role_pilihan == 1:
            role = "pemilik_toko"
            nama = input("Silakan Masukkan Nama : ")
            pin = input("Silakan Masukkan Pin: ")
            os.system("cls")

        elif role_pilihan == 2:
            role = "penjual"
            nama = input("Silakan Masukkan Nama : ")
            pin = input("Silakan Masukkan Pin: ")
            os.system("cls")

        elif role_pilihan == 3:
            os.system("cls")
            print("Terima Kasih Telah Menggunakan Aplikasi Kami!!")
            exit()  

        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            main()

        for account in akun:
            if account["role"] == role and account["nama"] == nama and account["pin"] == pin:
                print(f"Login Berhasil! Selamat datang, {nama}.")
                os.system("cls")
                interface_pemilik() if role == "pemilik_toko" else interface_penjual()
                return
            
        print("Login gagal. Silakan coba lagi.")
        input("Tekan enter untuk kembali")
        os.system("cls")
        main()
            
    except ValueError:
        print("Masukkan pilihan yang valid!")