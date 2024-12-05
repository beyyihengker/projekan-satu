# Fungsi untuk mendapatkan saldo terbaru
def saldo_terbaru():
    keuangan = baca_csv(file_path_keuangan)
    return int(keuangan[-1]["saldo"]) if keuangan else 0

# Fungsi untuk mencatat transaksi keuangan
def transaksi_keuangan(keterangan, jumlah):
    keuangan = baca_csv(file_path_keuangan)
    saldo_sekarang = saldo_terbaru()
    saldo_baru = saldo_sekarang + jumlah
    now = datetime.now()

    keuangan.append({
        "tanggal": now.strftime("%Y-%m-%d"),
        "keterangan": keterangan,
        "jumlah": str(jumlah),
        "saldo": str(saldo_baru)
    })
    write_csv(file_path_keuangan, keuangan, ["tanggal", "keterangan", "jumlah", "saldo"])
