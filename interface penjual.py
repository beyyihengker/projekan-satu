# Fungsi antarmuka penjual
def interface_penjual():
    while True:
        print("\n==========˖ ᡣ𐭩 ⊹ ࣪  ౨ৎ˚₊==========")
        print("==== Selamat Datang, Penjual ====")
        print("=====   Menu Pemilik Toko   =====")
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
            stok = baca_csv(file_path_stok)
            penjualan = baca_csv(file_path_penjualan)
            os.system("cls")
            print("\n=== Pembayaran ===")

            total_transaksi = 0
            items_beli = []

            while True:
                nama = input("Masukkan nama tanaman (atau ketik 'selesai' untuk menyelesaikan): ").strip()
                if nama.lower() == "selesai":
                    break

                jumlah = int(input("Masukkan jumlah pembelian: "))

                # Periksa apakah nama tanaman ada di stok
                for item in stok:
                    if item["nama_tanaman"].lower() == nama.lower():
                        tanaman_ditemukan = True
                        if int(item["stok"]) >= jumlah:
                            total_harga = int(item["harga_jual"]) * jumlah
                            item["stok"] = str(int(item["stok"]) - jumlah)

                            # Simpan item yang dibeli
                            items_beli.append({
                                "nama_tanaman": nama,
                                "jumlah": jumlah,
                                "total_harga": total_harga
                            })
                            total_transaksi += total_harga
                            print(f"Berhasil menambahkan {nama} (x{jumlah}). Subtotal: Rp{total_transaksi}")
                        else:
                            print("Stok tidak mencukupi.")
                        break

                if not tanaman_ditemukan:
                    print("Tanaman tidak ditemukan.")

            if items_beli:
                # Rekam transaksi penjualan
                now = datetime.now()
                for item_beli in items_beli:
                    penjualan.append({
                        "nama_tanaman": item_beli["nama_tanaman"],
                        "jumlah": str(item_beli["jumlah"]),
                        "total_harga": str(item_beli["total_harga"]),
                        "tanggal": now.strftime("%Y-%m-%d"),
                        "waktu": now.strftime("%H:%M:%S")
                    })

                # Simpan perubahan ke file CSV
                write_csv(file_path_stok, stok, ["nama_tanaman", "stok", "harga_beli", "harga_jual"])
                write_csv(file_path_penjualan, penjualan, ["nama_tanaman", "jumlah", "total_harga", "tanggal", "waktu"])
        
                print(f"Pembayaran selesai! Total transaksi: Rp{total_transaksi}")
            else:
                print("Tidak ada item yang dibeli.")

            input("Tekan enter untuk kembali")
            os.system("cls")
        
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