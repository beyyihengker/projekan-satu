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
