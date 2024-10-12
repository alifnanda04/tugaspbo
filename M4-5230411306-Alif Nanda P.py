debitur = {}
pinjaman = {}

def tambah_debitur(nama, ktp, batas_pinjaman):
    if ktp in debitur:
        return "Debitur sudah ada dengan KTP ini."
    debitur[ktp] = {
        'nama': nama,
        'batas_pinjaman': batas_pinjaman
    }
    return f"Debitur {nama} berhasil ditambahkan."

def cari_debitur(kunci_pencarian):
    hasil = []
    for ktp, data_debitur in debitur.items():
        if (kunci_pencarian.lower() in data_debitur['nama'].lower() or
            kunci_pencarian == ktp):
            hasil.append({**data_debitur, 'ktp': ktp})
    return hasil if hasil else "Debitur tidak ditemukan."

def tambah_pinjaman(ktp, jumlah, bunga, bulan):
    if ktp not in debitur:
        return "Debitur tidak ditemukan."
    if jumlah > debitur[ktp]['batas_pinjaman']:
        return "Jumlah pinjaman melebihi batas."
    total_bunga = jumlah * bunga * bulan / 100
    total_pembayaran = jumlah + total_bunga
    pinjaman[ktp] = {
        'jumlah': jumlah,
        'bunga': bunga,
        'bulan': bulan,
        'total_pembayaran': total_pembayaran
    }
    return f"Pinjaman berhasil ditambahkan untuk debitur dengan KTP {ktp}."

def tampilkan_pinjaman():
    if not pinjaman:
        return "Tidak ada pinjaman untuk ditampilkan."
    for ktp, data_pinjaman in pinjaman.items():
        print(f"KTP Debitur: {ktp}")
        print(f"Jumlah Pinjaman: {data_pinjaman['jumlah']}")
        print(f"Bunga: {data_pinjaman['bunga']}%")
        print(f"Bulan: {data_pinjaman['bulan']}")
        print(f"Total Pembayaran: {data_pinjaman['total_pembayaran']}")
        print("-" * 30)

def menu():
    while True:
        print("\n=== Sistem Manajemen Debitur dan Pinjaman ===")
        print("1. Tambah Debitur")
        print("2. Cari Debitur")
        print("3. Tambah Pinjaman")
        print("4. Tampilkan Pinjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama debitur: ")
            ktp = input("Masukkan KTP debitur: ")
            batas_pinjaman = float(input("Masukkan batas pinjaman: "))
            print(tambah_debitur(nama, ktp, batas_pinjaman))
        
        elif pilihan == "2":
            kunci = input("Masukkan nama atau KTP debitur yang ingin dicari: ")
            hasil = cari_debitur(kunci)
            if isinstance(hasil, list):
                for deb in hasil:
                    print(f"Nama: {deb['nama']}, KTP: {deb['ktp']}, Batas Pinjaman: {deb['batas_pinjaman']}")
            else:
                print(hasil)
        
        elif pilihan == "3":
            ktp = input("Masukkan KTP debitur: ")
            jumlah = float(input("Masukkan jumlah pinjaman: "))
            bunga = float(input("Masukkan persentase bunga: "))
            bulan = int(input("Masukkan durasi pinjaman (bulan): "))
            print(tambah_pinjaman(ktp, jumlah, bunga, bulan))
        
        elif pilihan == "4":
            tampilkan_pinjaman()
        
        elif pilihan == "5":
            print("Anda Meninggalkan Program")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()