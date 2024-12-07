# Fungsi untuk mencatat transaksi keuangan dan menulis data ke file CSV.
def transaksi_keuangan(keterangan, jumlah):
    keuangan = baca_csv(file_path_keuangan)
    saldo_sekarang = saldo_terbaru()
    saldo_baru = saldo_sekarang + jumlah
    now = datetime.now()

    keuangan.append({
        "tanggal": now.strftime("%Y-%m-%d"),
        "waktu": now.strftime("%H:%M:%S"),
        "keterangan": keterangan,
        "jumlah": f"{jumlah}",
        "saldo": f"{saldo_baru}"
    })

    write_csv(file_path_keuangan, keuangan, ["tanggal", "waktu", "keterangan", "jumlah", "saldo"])
