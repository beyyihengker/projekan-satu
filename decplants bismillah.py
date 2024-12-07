import csv
import os
from datetime import datetime
import pandas as pd
from tabulate import tabulate

file_path_akun = "akun.csv"
file_path_stok = "stok.csv"
file_path_penjualan = "penjualan.csv"
file_path_keuangan = "keuangan.csv"

# Fungsi untuk menulis data ke file CSV.
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

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
    if not os.path.exists(file_path_keuangan):
        with open(file_path_keuangan, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["tanggal", "waktu", "keterangan", "jumlah", "saldo"])
            writer.writerow([datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"), "Saldo Awal", "0", "0"])

# Fungsi untuk menulis data ke CSV
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Fungsi untuk membaca data CSV
def baca_csv(file_path):
    data = []
    if os.path.exists(file_path):
        with open(file_path, mode="r") as file:
            baca = csv.DictReader(file)
            for row in baca:
                data.append(row)
    return data

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
        ["2", "Pegawai"],
        ["3", "Keluar Aplikasi"]
    ]

    print(tabulate(menu_utama, headers=["No", "Menu"], tablefmt="double_grid"))

    try:
        role_pilihan = int(input("Silakan Pilih Opsi Antara 1/2/3: "))

        if role_pilihan == 1:
            role = "pemilik_toko"
            nama = input("Silakan Masukkan Nama : ")
            pin = input("Silakan Masukkan Pin: ")
            
        elif role_pilihan == 2:
            role = "penjual"
            nama = input("Silakan Masukkan Nama : ")
            pin = input("Silakan Masukkan Pin: ")
            
        elif role_pilihan == 3:
            os.system("cls")
            print("Terima Kasih Telah Menggunakan Aplikasi Kami!!")
            exit()  

        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            main()

    except ValueError:
        print("Masukkan pilihan yang valid!")
        input("Tekan enter untuk melanjutkan.")
        os.system("cls")
        main()

    while True:
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
            
# Fungsi antarmuka pemilik toko
def interface_pemilik():
    while True:
        print("\n==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊==========")
        print("==== Selamat Datang, Pemilik ====")
        print("=====   Menu Pemilik Toko   =====")
        print("==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊==========")
        menu_pemilik = [
            ["1", "Stok Produk"],
            ["2", "Laporan Keuangan"],
            ["3", "Tambah Pegawai"],
            ["4", "History Penjualan"],
            ["5", "Logout"],
            ["6", "Keluar Aplikasi"]
        ]

        print(tabulate(menu_pemilik, headers=["No", "Menu"], tablefmt="double_grid"))

        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            os.system("cls")
            kelola_stok()
        
        elif pilihan == "2":
            os.system("cls")
            keuangan = pd.read_csv('keuangan.csv')
            print("\n=== Laporan Keuangan ===")
            print(tabulate(keuangan.values.tolist(), headers=["Tanggal", "Waktu", "Keterangan", "Jumlah", "Saldo"], tablefmt="double_grid"))
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_pemilik()

        elif pilihan == "3":
            os.system("cls")
            buat_akun()
        
        elif pilihan == "4":
            penjualan = pd.read_csv(file_path_penjualan)
            os.system("cls")
            print("\n=== History Penjualan ===")
            print(tabulate(penjualan, headers=["No", "Tanaman", "Jumlah", "Total", "Tanggal", "Waktu"], tablefmt="double_grid"))
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_pemilik()
        
        elif pilihan == "5":
            os.system("cls")
            main()
        
        elif pilihan == "6":
            os.system("cls")
            print("Keluar dari aplikasi...")
            exit()
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_pemilik()

# Fungsi untuk memanggil sub menu Stok Produk si Pemilik
def kelola_stok():
    while True:
        print("\n======˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊======")
        print("=== Menu Stok Produk ===")
        print("======˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊======")
        menu_stok= [
        ["1", "Lihat Stok"],
        ["2", "Tambah Stok"],
        ["3", "Ubah Stok"],
        ["4", "Hapus Stok"],
        ["5", "Kembali"]
        ]

        print(tabulate(menu_stok, headers=["No", "Menu"], tablefmt="double_grid"))

        pilihan = input("Pilih submenu: ")

        if pilihan == "1":
            os.system("cls")
            stok = pd.read_csv('stok.csv')
            print("\n=== List Stok ===")
            print(tabulate(stok.values.tolist(), headers=["Nama Tanaman","Jumlah Stok","Harga Beli","Harga Jual"], tablefmt="double_grid"))
            input("Tekan enter untuk kembali")
            os.system("cls")
            kelola_stok()

        elif pilihan == "2":
            os.system("cls")
            print("\n=== Tambah Stok ===")
            list_stok = pd.read_csv('stok.csv')
            print(tabulate(list_stok.values.tolist(), headers=["Nama Tanaman","Jumlah Stok","Harga Beli","Harga Jual"], tablefmt="double_grid"))

            # Fungsi untuk validasi input angka
            def input_angka(prompt):
                while True:
                    value = input(prompt)
                    if value.strip() == "":
                        print("Input tidak boleh kosong. Silakan coba lagi.")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        kelola_stok()
                    elif not value.isdigit():
                        print("Input harus berupa angka positif. Silakan coba lagi.")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        kelola_stok()
                    else:
                        return int(value)

            # Fungsi untuk validasi input string
            def input_string(prompt):
                while True:
                    value = input(prompt)
                    if value.strip() == "":
                        print("Input tidak boleh kosong. Silakan coba lagi.")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        kelola_stok()
                    else:
                        return value

            # Input dengan validasi
            nama_tanaman = input_string("Masukkan nama tanaman: ")
            stok1 = input_angka("Masukkan jumlah stok: ")
            harga_beli = input_angka("Masukkan harga beli: ")
            harga_jual = input_angka("Masukkan harga jual: ")

            # Hitung total harga beli
            total_harga_beli = stok1 * harga_beli

            # Baca saldo terakhir dari keuangan.csv
            keuangan = pd.read_csv(file_path_keuangan)
            if keuangan.empty:
                saldo_sekarang = 0
            else:
                saldo_sekarang = float(keuangan.iloc[-1]['saldo'])

            # Periksa apakah saldo cukup
            if saldo_sekarang < total_harga_beli:
                print("Saldo tidak mencukupi untuk menambah stok.")
                input("Tekan enter untuk kembali")
                os.system("cls")
                kelola_stok()

            # Tambahkan data ke stok.csv
            stok = pd.read_csv(file_path_stok)
            stok = stok._append({"nama_tanaman": nama_tanaman, "stok": stok1, "harga_beli": harga_beli, "harga_jual": harga_jual}, ignore_index=True)
            stok.to_csv(file_path_stok, index=False)

            # Kurangi saldo dan catat transaksi ke keuangan.csv
            saldo_baru = saldo_sekarang - total_harga_beli
            now = datetime.now()
            keuangan = keuangan._append({
                "tanggal": now.strftime("%Y-%m-%d"),
                "waktu": now.strftime("%H:%M:%S"),
                "keterangan": f"Pembelian {nama_tanaman} dengan jumlah ({stok1} pcs)",
                "jumlah": -total_harga_beli,
                "saldo": saldo_baru
            }, ignore_index=True)
            keuangan.to_csv(file_path_keuangan, index=False)

            print(f"Stok berhasil ditambahkan. Total pengeluaran: Rp{total_harga_beli}")
            input("Tekan enter untuk kembali")
            os.system("cls")
            kelola_stok()

        elif pilihan == "3":
            os.system("cls")
            print("\n=== Ubah Stok ===")

            # Tampilkan daftar stok
            stok = baca_csv(file_path_stok)
            list_stok = pd.read_csv('stok.csv')
            print(tabulate(list_stok.values.tolist(), headers=["Nama Tanaman", "Jumlah Stok", "Harga Beli", "Harga Jual"], tablefmt="double_grid"))

            # Fungsi untuk validasi input angka
            def input_angka(prompt, default_value=None):
                while True:
                    value = input(prompt)
                    if value.strip() == "":
                        if default_value is not None:
                            return default_value
                        else:
                            print("Input tidak boleh kosong. Silakan coba lagi.")
                            input("Tekan enter untuk kembali")
                            os.system("cls")
                            kelola_stok()
                    elif not value.isdigit():
                        print("Input harus berupa angka positif. Silakan coba lagi.")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        kelola_stok()
                    else:
                        return int(value)

            # Fungsi untuk validasi input string
            def input_string(prompt, default_value=None):
                while True:
                    value = input(prompt)
                    if value.strip() == "":
                        if default_value is not None:
                            return default_value
                        else:
                            print("Input tidak boleh kosong. Silakan coba lagi.")
                            input("Tekan enter untuk kembali")
                            os.system("cls")
                            kelola_stok()
                    else:
                        return value

            # Input nama tanaman yang akan diubah
            nama_tanaman = input_string("Masukkan nama tanaman yang akan diubah: ")

            # Periksa dan ubah data stok
            for item in stok:
                if item['nama_tanaman'].lower() == nama_tanaman.lower():
                    # Input stok baru dengan validasi
                    nama_tanaman_baru = input_string(f"Masukkan nama tanaman yang baru (sebelumnya: {item['nama_tanaman']}): ", default_value=item['nama_tanaman'])
                    stok_baru = input_angka(f"Masukkan stok yang baru (sebelumnya: {item['stok']}): ", default_value=int(item['stok']))
                    harga_beli_baru = input_angka(f"Masukkan harga beli yang baru (sebelumnya: {item['harga_beli']}): ", default_value=int(item['harga_beli']))
                    harga_jual_baru = input_angka(f"Masukkan harga jual yang baru (sebelumnya: {item['harga_jual']}): ", default_value=int(item['harga_jual']))

                    # Update data
                    item['nama_tanaman'] = nama_tanaman_baru
                    item['stok'] = stok_baru
                    item['harga_beli'] = harga_beli_baru
                    item['harga_jual'] = harga_jual_baru

                    # Simpan perubahan ke file CSV
                    write_csv(file_path_stok, stok, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                    print("Data berhasil diubah.")
                    break
            else:
                print("Tanaman tidak ditemukan.")

            input("Tekan enter untuk kembali")
            os.system("cls")
            kelola_stok()

        elif pilihan == "4":
            os.system("cls")
            stok = baca_csv(file_path_stok)
            list_stok = pd.read_csv('stok.csv')
            print("\n=== Hapus Stok ===")
            print(tabulate(list_stok.values.tolist(), headers=["Nama Tanaman","Jumlah Stok","Harga Beli","Harga Jual"], tablefmt="double_grid"))
            nama_tanaman = input("Masukkan nama tanaman yang akan dihapus: ")
            stok_terbaru = [item for item in stok if item['nama_tanaman'].lower() != nama_tanaman.lower()]

            if len(stok_terbaru) < len(stok):
                write_csv(file_path_stok, stok_terbaru, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                print("Stok berhasil dihapus.")
                input("Tekan enter untuk kembali")
                os.system("cls")
            else:
                print("Tanaman tidak ditemukan.")
                input("Tekan enter untuk kembali")
                os.system("cls")
                kelola_stok()

        elif pilihan == "5":
            os.system("cls")
            interface_pemilik()
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")

# Fungsi untuk menambahkan user baru
def buat_akun(akun_csv=file_path_akun):
    os.system("cls")
    print("\n=== Tambah Pegawai ===")
    menu_role_baru = [
        ["1", "Role Pemilik Toko"],
        ["2", "Role Penjual"],
        ["3", "Hapus User"],
        ["4", "Kembali"]
    ]
    print(tabulate(menu_role_baru, headers=["No", "Menu"], tablefmt="double_grid"))

    role_baru = int(input("Silakan Pilih Opsi Antara 1/2/3/4: "))
    if role_baru == 1:
            role_baru = "pemilik_toko"
    elif role_baru == 2:
            role_baru = "penjual"
    elif role_baru == 3:
            os.system("cls")
            hapus_akun(akun_csv)
    elif role_baru == 4:
            os.system("cls")
            interface_pemilik()
            return
    else:
            raise ValueError

    pegawai_baru = input("Silakan Masukkan Nama : ")
    if not pegawai_baru:
            print("Nama tidak boleh kosong!")
            input("Tekan enter untuk melanjutkan.")
            os.system("cls")
            buat_akun()
            return
    if pegawai_baru in [row['nama'] for row in baca_csv(akun_csv)]:
            print("Nama sudah ada di database!")
            input("Tekan enter untuk melanjutkan.")
            os.system("cls")
            buat_akun()
            return
        
    while True:
            try:
                pin = int(input("Silakan Masukkan Pin: "))
                break
            except ValueError:
                print("Pin harus dalam bentuk angka!")
                input("Tekan enter untuk melanjutkan.")
                os.system("cls")
                buat_akun()

    akun = pd.read_csv(akun_csv)
    akun = akun._append({"role": role_baru, "nama": pegawai_baru, "pin": pin}, ignore_index=True)
    akun.to_csv(akun_csv, index=False)
    print("Pegawai baru telah ditambahkan.")

    input("Tekan enter untuk melanjutkan.")
    os.system("cls")
    buat_akun()
    
# Fungsi untuk menghapus user
def hapus_akun(akun_csv=file_path_akun):
    akun = pd.read_csv(akun_csv)
    print("\n=== Hapus Pegawai ===")
    print(tabulate(akun.values.tolist(), headers=["Role", "Nama", "Pin"], tablefmt="double_grid"))
    pegawai_hapus = input("Masukkan nama pegawai yang ingin dihapus: ")
    akun = akun[akun["nama"] != pegawai_hapus]
    akun.to_csv(akun_csv, index=False)
    print("Pegawai berhasil dihapus.")
    input("Tekan enter untuk melanjutkan.")
    os.system("cls")
    buat_akun()

# Fungsi untuk mendapatkan saldo terbaru dari file CSV.
def saldo_terbaru():
    keuangan = baca_csv(file_path_keuangan)
    if not keuangan:
        return 0
    return float(keuangan[-1]["saldo"])

# Fungsi untuk mencatat transaksi keuangan dan menulis data ke file CSV.
def transaksi_keuangan(keterangan, jumlah):
    keuangan = baca_csv(file_path_keuangan)
    saldo_sekarang = saldo_terbaru()
    saldo_baru = saldo_sekarang + jumlah
    now = datetime.now()

    keuangan.append({
        "tanggal": now.strftime("%Y-%m-%d"),
        "waktu": now.strftime("%H:%M:%S"),
        "keterangan": keterangan,
        "jumlah": f"{jumlah}",
        "saldo": f"{saldo_baru}"
    })

    write_csv(file_path_keuangan, keuangan, ["tanggal", "waktu", "keterangan", "jumlah", "saldo"])

# Fungsi antarmuka penjual
def interface_penjual():
    while True:
        print("\n==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊==========")
        print("==== Selamat Datang, Pegawai ====")
        print("=====   Menu Pegawai Toko   =====")
        print("==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊==========")
        menu_penjual =[
            ["1", "Daftar Barang"],
            ["2", "Pembayaran"],
            ["3", "Logout"],
            ["4", "Keluar Aplikasi"]
        ]

        print(tabulate(menu_penjual, headers=["No", "Menu"], tablefmt="double_grid")) 
    
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            os.system("cls")
            stok = pd.read_csv('stok.csv')
            print("\n=== Daftar Barang ===")
            print(tabulate(stok.values.tolist(), headers=["Nama Tanaman","Jumlah Stok","Harga Beli","Harga Jual"], tablefmt="double_grid"))
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_penjual()

        elif pilihan == "2":
            os.system("cls")
            stok = baca_csv(file_path_stok)
            penjualan = baca_csv(file_path_penjualan)
            list_stok = pd.read_csv('stok.csv')
            print(tabulate(list_stok.values.tolist(), headers=["Nama Tanaman", "Jumlah Stok", "Harga Beli", "Harga Jual"], tablefmt="double_grid"))
            print("\n=== Pembayaran ===")
            nama = input("Masukkan nama tanaman: ")
            jumlah = int(input("Masukkan jumlah pembelian: "))
            
            # Periksa apakah nama tanaman ada di stok
            tanaman_ditemukan = False
            for item in stok:
                if item["nama_tanaman"].lower() == nama.lower():
                    tanaman_ditemukan = True

                    # Periksa stok mencukupi
                    if int(item["stok"]) >= jumlah:
                        total_harga = int(item["harga_jual"]) * jumlah
                        item["stok"] = str(int(item["stok"]) - jumlah)
                        
                        # Rekam transaksi penjualan
                        now = datetime.now()
                        penjualan.append({
                            "nama_tanaman": nama,
                            "jumlah": str(jumlah),
                            "total_harga": str(total_harga),
                            "tanggal": now.strftime("%Y-%m-%d"),
                            "waktu": now.strftime("%H:%M:%S")
                        })
                        
                        # Rekam transaksi keuangan
                        transaksi_keuangan(
                            keterangan=f"Penjualan {nama} dengan jumlah ({jumlah} pcs)", 
                            jumlah=total_harga
                        )

                        # Simpan perubahan pada file CSV
                        write_csv(file_path_stok, stok, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                        write_csv(file_path_penjualan, penjualan, ["nama_tanaman", "jumlah", "total_harga", "tanggal", "waktu"])
                        print(f"Pembayaran berhasil! Total: Rp{total_harga}")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        interface_penjual()
                    
                    else:
                        print("Stok tidak mencukupi.")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        interface_penjual()
            
            if not tanaman_ditemukan:
                print("Tanaman tidak ditemukan.")
                input("Tekan enter untuk kembali")
                os.system("cls")
                interface_penjual()

        elif pilihan == "3":
            os.system("cls")
            main()
        
        elif pilihan == "4":
            os.system("cls")
            print("Keluar dari aplikasi...")
            exit()
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_penjual()

# Jalankan program
if __name__ == "__main__":
    main()
