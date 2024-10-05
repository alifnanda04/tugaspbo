class DaftarMenu:
    def __init__(self):
        self.menu = {
            'makanan': [],
            'minuman': []
        }

    def tambah_makanan(self, makanan):
        self.menu['makanan'].append(makanan)
        print(f"{makanan} telah ditambahkan ke daftar makanan.")

    def tambah_minuman(self, minuman):
        self.menu['minuman'].append(minuman)
        print(f"{minuman} telah ditambahkan ke daftar minuman.")

    def tampilkan_menu(self):
        print("\nDaftar Menu:")
        print("Makanan:")
        for makanan in self.menu['makanan']:
            print(f"- {makanan}")
        
        print("Minuman:")
        for minuman in self.menu['minuman']:
            print(f"- {minuman}")

    def menu_interaktif(self):
        while True:
            print("\nPilih opsi:")
            print("1. Tambah Makanan")
            print("2. Tambah Minuman")
            print("3. Tampilkan Menu")
            print("4. Keluar")

            pilihan = input("Masukkan pilihan (1/2/3/4): ")

            if pilihan == '1':
                makanan = input("Masukkan nama makanan: ")
                self.tambah_makanan(makanan)
            elif pilihan == '2':
                minuman = input("Masukkan nama minuman: ")
                self.tambah_minuman(minuman)
            elif pilihan == '3':
                self.tampilkan_menu()
            elif pilihan == '4':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan dipilih orang lain.")

# Contoh penggunaan
daftar_menu = DaftarMenu()
daftar_menu.menu_interaktif()