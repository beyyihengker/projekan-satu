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
            nama_tanaman = input("Masukkan nama tanaman: ")
            stok1 = input("Masukkan jumlah stok: ")
            harga_beli = input("Masukkan harga beli: ")
            harga_jual = input("Masukkan harga jual: ")

            stok = pd.read_csv(file_path_stok)
            stok = stok._append({"nama_tanaman": nama_tanaman, "stok": stok1, "harga_beli": harga_beli,"harga_jual": harga_jual},ignore_index=True)
            stok.to_csv(file_path_stok,index=False)
            print("Stok berhasil ditambahkan.")
            input("Tekan enter untuk kembali")
            os.system("cls")
            kelola_stok()

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
            kelola_stok()

        elif pilihan == "4":
            os.system("cls")
            print("\n=== Hapus Stok ===")
            nama_tanaman = input("Masukkan nama tanaman yang akan dihapus: ")
            stok = baca_csv(file_path_stok)
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