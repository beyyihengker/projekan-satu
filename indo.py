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

# Fungsi antarmuka pemilik toko
def interface_pemilik():
    while True:
        print("==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊=========")
        print("==== Selamat Datang, Saviya ====")
        print("=====  Menu Pemilik Toko   =====")
        print("       1. Stok Produk          ")
        print("       2. Laporan Keuangan     ")
        print("       3. Tambah Pegawai       ")
        print("       4. History Penjualan    ")
        print("       5. Logout               ")
        print("       6. Keluar Aplikasi      ")
        print("==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊=========")

        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            os.system("cls")
            kelola_stok()
        
        elif pilihan == "2":
            keuangan = baca_csv(file_path_keuangan)
            if keuangan:
                print("\nLaporan Keuangan".center(50))
                for record in keuangan:
                    print(f"{record['tanggal']} - {record['keterangan']} - Jumlah: {record['jumlah']} - Saldo: {record['saldo']}")
            else:
                print("Tidak ada catatan keuangan.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_pemilik()

        elif pilihan == "3":
            def buat_akun():
                os.system("cls")
                role_baru = input("Masukkan role baru (0 untuk kembali) : ")
                if role_baru == "0":
                    interface_pemilik()

                pegawai_baru = input("Masukkan nama pegawai baru : ")
                pin = input("Masukkan pin pegawai baru : ")

                while not (role_baru and pegawai_baru and pin):
                    print("Role, nama dan pin harus diisi.")
                    role_baru = input("Masukkan role baru: ")
                    pegawai_baru = input("Masukkan nama pegawai baru : ")
                    pin = input("Masukkan pin pegawai baru : ")

                try:
                    pin = int(pin)
                except ValueError:
                    print("Pin harus berupa angka.")
                    lanjut = input("Tekan enter untuk melanjutkan")
                    os.system('cls')
                    return buat_akun()

                akun = baca_csv(file_path_akun)
                akun.append({"role": role_baru, "nama": pegawai_baru, "pin": str(pin)})
                write_csv(file_path_akun, akun, ["role", "nama", "pin"])
                print("Pegawai baru telah ditambahkan.")
                input("Tekan enter untuk melanjutkan.")
                os.system("cls")
            
            buat_akun()
        
        elif pilihan == "4":
            penjualan = baca_csv(file_path_penjualan)
            os.system("cls")
            print("\n=== History Penjualan ===")
            for sale in penjualan:
                print(f"Tanaman: {sale['nama_tanaman']}, Jumlah: {sale['jumlah']}, Total: {sale['total_harga']}, Tanggal: {sale['tanggal']}, Waktu: {sale['waktu']}")
                input("Tekan enter untuk kembali")
                os.system("cls")
                interface_pemilik()
        
        elif pilihan == "5":
            os.system("cls")
            main()
        
        elif pilihan == "6":
            print("Keluar dari aplikasi...")
            break
        
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
        print("    1. Lihat Stok       ")
        print("    2. Tambah Stok      ")
        print("    3. Ubah Stok        ")
        print("    4. Hapus Stok       ")
        print("    5. Kembali          ")
        print("======˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊======")

        pilihan = input("Pilih submenu: ")

        if pilihan == "1":
            os.system("cls")
            print("\n=== Lihat Stok ===")
            stok = baca_csv(file_path_stok)
            if stok:
                for item in stok:
                    print(f"Nama: {item['nama_tanaman']}, Stok: {item['stok']}, Harga Beli: {item['harga_beli']}, Harga Jual: {item['harga_jual']}")
            else:
                print("Stok kosong.")
            input("Tekan enter untuk kembali")
            os.system("cls")

        elif pilihan == "2":
            os.system("cls")
            print("\n=== Tambah Stok ===")
            nama_tanaman = input("Masukkan nama tanaman: ")
            stok = input("Masukkan jumlah stok: ")
            harga_beli = input("Masukkan harga beli: ")
            harga_jual = input("Masukkan harga jual: ")

            stok = baca_csv(file_path_stok)
            stok.append({
                "nama_tanaman": nama_tanaman,
                "stok": stok,
                "harga_beli": harga_beli,
                "harga_jual": harga_jual
            })
            write_csv(file_path_stok, stok, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
            print("Stok berhasil ditambahkan.")
            input("Tekan enter untuk kembali")
            os.system("cls")

        elif pilihan == "3":
            os.system("cls")
            print("\n=== Ubah Stok ===")
            nama_tanaman = input("Masukkan nama tanaman yang akan diubah: ")
            stok = baca_csv(file_path_stok)

            for item in stok:
                if item['nama_tanaman'].lower() == nama_tanaman.lower():
                    print(f"Data saat ini: Stok: {item['stok']}, Harga Beli: {item['harga_beli']}, Harga Jual: {item['harga_jual']}")
                    item['stok'] = input("Masukkan stok baru: ") or item['stok']
                    item['harga_beli'] = input("Masukkan harga beli baru: ") or item['harga_beli']
                    item['harga_jual'] = input("Masukkan harga jual baru: ") or item['harga_jual']
                    write_csv(file_path_stok, stok, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                    print("Data berhasil diubah.")
                    break
            else:
                print("Tanaman tidak ditemukan.")
            input("Tekan enter untuk kembali")
            os.system("cls")

        elif pilihan == "4":
            os.system("cls")
            print("\n=== Hapus Stok ===")
            nama_tanaman = input("Masukkan nama tanaman yang akan dihapus: ")
            stok = baca_csv(file_path_stok)
            stok_terbaru = [item for item in stok if item['nama_tanaman'].lower() != nama_tanaman.lower()]

            if len(stok_terbaru) < len(stok):
                write_csv(file_path_stok, stok_terbaru, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                print("Stok berhasil dihapus.")
            else:
                print("Tanaman tidak ditemukan.")
                input("Tekan enter untuk kembali")
            os.system("cls")

        elif pilihan == "5":
            os.system("cls")
            return
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")

# Fungsi untuk mendapatkan saldo terbaru
def saldo_terbaru():
    keuangan = baca_csv(file_path_keuangan)
    return int(keuangan[-1]["saldo"]) if keuangan else 0

# Fungsi untuk mencatat transaksi keuangan
def transaksi_keuangan(keterangan, jumlah):
    keuangan = baca_csv(file_path_keuangan)
    saldo_sekarang = saldo_terbaru()
    saldo_baru = saldo_sekarang + jumlah
    now = datetime.now()

    keuangan.append({
        "tanggal": now.strftime("%Y-%m-%d"),
        "keterangan": keterangan,
        "jumlah": str(jumlah),
        "saldo": str(saldo_baru)
    })
    write_csv(file_path_keuangan, keuangan, ["tanggal", "keterangan", "jumlah", "saldo"])

# Fungsi antarmuka penjual
def interface_penjual():
    while True:
        print("\n=====˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊====")
        print("==== Menu Penjual ====")
        print("   1. Harga Produk    ")
        print("   2. Daftar Barang   ")
        print("   3. Pembayaran      ")
        print("   4. Logout          ")
        print("   5. Keluar Aplikasi ")
        print("=====˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊====")  
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            stok = baca_csv(file_path_stok)
            os.system("cls")
            print("\n=== Harga Produk ===")
            for item in stok:
                print(f"Nama: {item['nama_tanaman']}, Harga: {item['harga_jual']}")
                input("Tekan enter untuk kembali")
                os.system("cls")
                interface_penjual()
        
        elif pilihan == "2":
            stok = baca_csv(file_path_stok)
            os.system("cls")
            print("\n=== Daftar Barang ===")
            if stok:
                for item in stok:
                    print(f"Nama: {item['nama_tanaman']}, Stok: {item['stok']}")
            else:
                print("Tidak ada data barang.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_penjual()

        elif pilihan == "3":
            stok = baca_csv(file_path_stok)
            penjualan = baca_csv(file_path_penjualan)
            os.system("cls")
            print("\n=== Pembayaran ===")
            nama = input("Masukkan nama tanaman: ")
            jumlah = int(input("Masukkan jumlah pembelian: "))
            
            # Periksa apakah nama tanaman ada di stok
            for item in stok:
                if item["nama_tanaman"].lower() == nama.lower():

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
                        
                        # Simpan perubahan pada file CSV
                        write_csv(file_path_stok, stok, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                        write_csv(file_path_penjualan, penjualan, ["nama_tanaman", "jumlah", "total_harga", "tanggal", "waktu"])
                        
                        print(f"Pembayaran berhasil! Total: Rp{total_harga}")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        return
                    
                    else:
                        print("Stok tidak mencukupi.")
                        input("Tekan enter untuk kembali")
                        os.system("cls")
                        return
            else:
                print("Tanaman tidak ditemukan.")
                input("Tekan enter untuk kembali")
                os.system("cls")
                interface_penjual()
        
        elif pilihan == "4":
            os.system("cls")
            main()
        
        elif pilihan == "5":
            print("Keluar dari aplikasi...")
            break
        
        else:
            print("Pilihan tidak valid.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            interface_penjual()

# Jalankan program
if __name__ == "__main__":
    main()