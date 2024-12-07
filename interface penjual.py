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
