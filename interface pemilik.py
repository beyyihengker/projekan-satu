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