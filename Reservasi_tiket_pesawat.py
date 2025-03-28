def main():
    # Dictionary untuk menyimpan data penerbangan
    penerbangan = {
        "MLB200": {"tujuan": "Melbourne", "harga": 7341000, "kapasitas": 120},
        "TYO180": {"tujuan": "Tokyo", "harga": 5890000, "kapasitas": 90},
        "DXB160": {"tujuan": "Dubai", "harga": 5000000, "kapasitas": 70},
        "SIN140": {"tujuan": "Singapore", "harga": 1337000, "kapasitas": 50},
        "AMS120": {"tujuan": "Amsterdam", "harga": 9820000, "kapasitas": 30}
    }
    
    # Header sistem reservasi
    print("============== SISTEM RESERVASI TIKET PESAWAT ==============")
    print(" Selamat datang di layanan reservasi tiket pesawat online!")
    print(" Silakan isi data diri Anda untuk memulai pemesanan")
    
    # Loop untuk memungkinkan multiple pemesanan
    while True:
        # input data pelanggan
        print("\n====================== DATA PELANGGAN ======================")
        
        # Validasi input nama tidak boleh kosong
        nama = input("Nama Lengkap: ")
        while not nama:
            print("Nama tidak boleh kosong!")
            nama = input("Nama Lengkap: ")
            
        # Validasi format email harus mengandung '@' dan '.'
        email = input("Email: ")
        while "@" not in email or "." not in email:
            print("Format email tidak valid!")
            email = input("Email: ")
            
        no_hp = input("Nomor HP: ")

        # Menampilkan daftar penerbangan yang tersedia
        print("\n==================== DAFTAR PENERBANGAN ====================")
        print("-" * 60)
        print("No. Penerbangan|    Tujuan   | Harga Tiket  | Kursi Tersedia")
        print("-" * 60)
        
        # Perulangan for untuk menampilkan semua penerbangan
        for no_penerbangan, info in penerbangan.items():
            print(f"{no_penerbangan:14} | {info['tujuan']:11} | Rp {info['harga']:} | {info['kapasitas']:3} kursi")
        
        print("-" * 60)
        
        # pemesanan tiket
        while True:
            # Input nomor penerbangan (diubah ke uppercase)
            no_penerbangan = input("\nMasukkan nomor penerbangan: ").upper()
            
            # Validasi kode penerbangan
            if no_penerbangan not in penerbangan:
                print("Kode penerbangan tidak valid!")
                continue
                
            # Input jumlah tiket dengan validasi
            try:
                # Konversi string input ke integer
                jumlah = int(input("Jumlah tiket: "))
                if jumlah <= 0:
                    print("Minimal 1 tiket!")
                    continue
            except ValueError:  # Handle jika input bukan angka
                print("Harap masukkan angka!")
                continue
                
            # Cek ketersediaan kursi
            if jumlah > penerbangan[no_penerbangan]["kapasitas"]:
                print(f"Kursi tidak cukup! Tersisa {penerbangan[no_penerbangan]['kapasitas']} kursi")
                continue
                
            # Hitung total harga
            total = jumlah * penerbangan[no_penerbangan]["harga"]
            
            # Proses pembayaran
            print(f"\nTOTAL: Rp {total:,}")
            while True:
                try:
                    # Konversi nominal pembayaran ke integer
                    bayar = int(input("Masukkan nominal pembayaran: Rp "))
                    if bayar < total:
                        print("Pembayaran kurang!")
                        continue
                    break
                except ValueError:
                    print("Harap masukkan angka!")
            
            # Update kursi yang tersedia
            penerbangan[no_penerbangan]["kapasitas"] -= jumlah
            
            # Cetak struk pemesanan
            print("\n========= STRUK PEMESANAN =========")
            print("-" * 35)
            print("DATA PELANGGAN:")
            print("Nama    : ", nama)
            print("Email   : ", email)
            print("HP      : ", no_hp)
            
            print("\nDATA PENERBANGAN:")
            print("Nomor           :", no_penerbangan)
            print("Tujuan          :", penerbangan[no_penerbangan]['tujuan'])
            print("Harga per tiket : Rp", penerbangan[no_penerbangan]['harga'])
            print("Jumlah tiket    :", jumlah)
            print("Total           : Rp", total)
            print("Bayar           : Rp", bayar)
            print("Kembali         : Rp", bayar - total) 
            print("-" * 35)
            print("Pesanan berhasil!\n")
            print("Enjoy your flight!\n")
            break
        
        # Konfirmasi pemesanan lagi
        jawaban = input("Pesan lagi? (y/n): ")
        if jawaban != 'y' and jawaban != 'Y':
            print("Terima kasih!")
            break

if __name__ == "__main__":
    main()