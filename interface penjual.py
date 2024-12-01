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