# Fungsi untuk menambahkan user baru
def buat_akun(akun_csv=file_path_akun):
    os.system("cls")
    print("\n=== Tambah Pegawai ===")
    menu_role_baru = [
        ["1", "Role Pemilik Toko"],
        ["2", "Role Penjual"],
        ["3", "Hapus User"],
        ["4", "Kembali"]
    ]
    print(tabulate(menu_role_baru, headers=["No", "Menu"], tablefmt="double_grid"))

    try:
        role_baru = int(input("Silakan Pilih Opsi Antara 1/2/3/4: "))
        if role_baru == 1:
            role_baru = "pemilik_toko"
        elif role_baru == 2:
            role_baru = "penjual"
        elif role_baru == 3:
            os.system("cls")
            hapus_akun(akun_csv)
        elif role_baru == 4:
            os.system("cls")
            interface_pemilik()
            return
        else:
            raise ValueError

        pegawai_baru = input("Silakan Masukkan Nama : ")
        pin = input("Silakan Masukkan Pin: ")
        akun = pd.read_csv(akun_csv)
        akun = akun._append({"role": role_baru, "nama": pegawai_baru, "pin": str(pin)}, ignore_index=True)
        akun.to_csv(akun_csv, index=False)
        print("Pegawai baru telah ditambahkan.")
    except ValueError:
        print("Masukkan pilihan yang valid!")
        
    input("Tekan enter untuk melanjutkan.")
    os.system("cls")
    interface_pemilik()

# Fungsi untuk menghapus user
def hapus_akun(akun_csv=file_path_akun):
    akun = pd.read_csv(akun_csv)
    print("\n=== Hapus Pegawai ===")
    print(tabulate(akun.values.tolist(), headers=["Role", "Nama", "Pin"], tablefmt="double_grid"))
    pegawai_hapus = input("Masukkan nama pegawai yang ingin dihapus: ")
    akun = akun[akun["nama"] != pegawai_hapus]
    akun.to_csv(akun_csv, index=False)
    print("Pegawai berhasil dihapus.")
    input("Tekan enter untuk melanjutkan.")
    os.system("cls")
    buat_akun()