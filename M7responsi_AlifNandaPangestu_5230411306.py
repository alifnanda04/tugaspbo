class Pegawai:
    def _init_(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

class Produk:
    def _init_(self, kode_produk, nama_produk, harga, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.jenis_produk = jenis_produk

    def tampilkan_info(self):
        return f"{self.jenis_produk} - {self.nama_produk}: Rp{self.harga}"

class Snack(Produk):
    def _init_(self, kode_produk, nama_snack, harga):
        super()._init_(kode_produk, nama_snack, harga, "Snack")

class Makanan(Produk):
    def _init_(self, kode_produk, nama_makanan, harga):
        super()._init_(kode_produk, nama_makanan, harga, "Makanan")

class Minuman(Produk):
    def _init_(self, kode_produk, nama_minuman, harga):
        super()._init_(kode_produk, nama_minuman, harga, "Minuman")

class Transaksi:
    def _init_(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_list = []
        self.total_harga = 0

    def tambah_produk(self, produk, jumlah):
        self.produk_list.append((produk, jumlah))
        self.total_harga += produk.harga * jumlah

    def cetak_struk(self):
        print("\n=== STRUK PEMBELIAN ===")
        print(f"No Transaksi: {self.no_transaksi}")
        print(f"Nama Pegawai: {self.pegawai.nama}")
        print(f"Alamat Pegawai: {self.pegawai.alamat}")
        print("\nDaftar Produk:")
        for produk, jumlah in self.produk_list:
            print(f"- {produk.nama_produk} x{jumlah} : Rp{produk.harga * jumlah}")
        print(f"\nTotal Harga: Rp{self.total_harga}")
        print("=======================\n")

def menu():
    pegawai = Pegawai("001", "Budi", "Jl. Merdeka")
    produk_list = [
        Snack("S001", "Keripik Singkong", 10000),
        Makanan("M001", "Nasi Goreng", 20000),
        Minuman("D001", "Teh Botol", 5000),
    ]

    transaksi = None

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Buat Transaksi Baru")
        print("2. Tambah Produk ke Transaksi")
        print("3. Cetak Struk")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            no_transaksi = input("Masukkan No Transaksi: ")
            transaksi = Transaksi(no_transaksi, pegawai)
            print("Transaksi baru berhasil dibuat.")

        elif pilihan == "2":
            if transaksi is None:
                print("Buat transaksi terlebih dahulu!")
                continue

            print("\nDaftar Produk:")
            for i, produk in enumerate(produk_list):
                print(f"{i + 1}. {produk.tampilkan_info()}")

            pilihan_produk = int(input("Pilih produk (nomor): ")) - 1
            jumlah = int(input("Masukkan jumlah: "))

            if 0 <= pilihan_produk < len(produk_list):
                transaksi.tambah_produk(produk_list[pilihan_produk], jumlah)
                print("Produk berhasil ditambahkan ke transaksi.")
            else:
                print("Pilihan produk tidak valid.")

        elif pilihan == "3":
            if transaksi is None:
                print("Buat transaksi terlebih dahulu!")
            else:
                transaksi.cetak_struk()

        elif pilihan == "4":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")


menu()