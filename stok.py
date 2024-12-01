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