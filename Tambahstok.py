import csv
import os

# Nama file CSV
file_csv = 'stok_decplants.csv'

def buat_file_csv(file_csv):
    """Membuat file CSV jika belum ada."""
    if not os.path.exists(file_csv):
        with open(file_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama_Produk', 'Stok', 'Harga'])  # Header
            writer.writerow([1, 'Kaktus Mini', 10, 20000])
            writer.writerow([2, 'Bonsai', 5, 150000])
            writer.writerow([3, 'Sukulen', 7, 30000])
            print(f"File CSV '{file_csv}' berhasil dibuat dengan data awal.")

def tampilkan_produk(file_csv):
    """Menampilkan daftar produk dari file CSV."""
    try:
        with open(file_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Lewati header
            print("ID | Nama Produk       | Stok | Harga")
            print("---------------------------------------")
            for row in reader:
                print(f"{row[0]:<3}| {row[1]:<17}| {row[2]:<5}| Rp{row[3]:<8}")
    except FileNotFoundError:
        print("File CSV tidak ditemukan!")

def tambah_stok(file_csv, id_produk, jumlah_tambah):
    """Menambahkan stok pada produk berdasarkan ID."""
    try:
        data_baru = []
        produk_ditemukan = False

        # Baca file CSV
        with open(file_csv, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data_baru.append(header)

            for row in reader:
                if row[0] == str(id_produk):
                    produk_ditemukan = True
                    stok_lama = int(row[2])
                    row[2] = str(stok_lama + jumlah_tambah)  # Tambahkan stok
                data_baru.append(row)

        if not produk_ditemukan:
            print(f"Produk dengan ID {id_produk} tidak ditemukan.")
            return

        # Tulis ulang file CSV dengan stok diperbarui
        with open(file_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_baru)

        print(f"Stok produk dengan ID {id_produk} berhasil diperbarui!")
    except FileNotFoundError:
        print("File CSV tidak ditemukan!")
    except ValueError:
        print("Format data dalam file CSV salah!")

# Pembuatan file jika belum ada
buat_file_csv(file_csv)

# Tampilan menu utama
while True:
    print("\n=== Sistem Kasir DecPlants ===")
    print("1. Tampilkan Produk")
    print("2. Tambah Stok")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        tampilkan_produk(file_csv)
    elif pilihan == '2':
        try:
            id_produk = int(input("Masukkan ID produk: "))
            jumlah_tambah = int(input("Masukkan jumlah stok yang akan ditambahkan: "))
            tambah_stok(file_csv, id_produk, jumlah_tambah)
        except ValueError:
            print("Masukkan angka yang valid!")
    elif pilihan == '3':
        print("Terima kasih telah menggunakan sistem kasir DecPlants!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
