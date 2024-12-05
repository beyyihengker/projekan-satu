# Fungsi antarmuka pemilik toko
def interface_pemilik():
    while True:
        print("\n==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊==========")
        print("==== Selamat Datang, Saviya  ====")
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
            print(tabulate(keuangan.values.tolist(), headers=["Tanggal", "Keterangan", "Jumlah", "Saldo"], tablefmt="double_grid"))
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