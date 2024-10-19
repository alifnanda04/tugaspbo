class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def display(self):
        print(f"Judul: {self.judul}, Penyanyi: {self.penyanyi}, Genre: {self.genre}")


class MusicCollection:
    def __init__(self):
        self.collection = []

    def add_music(self, music):
        self.collection.append(music)
        print("Musik berhasil ditambahkan")

    def delete_music(self, judul):
        original_length = len(self.collection)
        self.collection = [m for m in self.collection if m.judul.lower() != judul.lower()]
        if len(self.collection) < original_length:
            print("Musik berhasil dihapus")
        else:
            print("Musik tidak ditemukan")

    def display_all(self):
        if not self.collection:
            print("Tidak ada musik dalam koleksi")
        else:
            for music in self.collection:
                music.display()

    def sort_music(self):
        self.collection.sort(key=lambda music: music.judul)
        print("Musik telah diurutkan dari A-Z berdasarkan judul")

    def search_music_by_artist(self, penyanyi):
        results = [m for m in self.collection if m.penyanyi.lower() == penyanyi.lower()]
        if not results:
            print("Tidak ditemukan musik dengan penyanyi tersebut")
        else:
            for music in results:
                music.display()


def main():
    collection = MusicCollection()

    while True:
        print("\nMenu:")
        print("1. Tambah Musik")
        print("2. Hapus Musik")
        print("3. Tampilkan Semua Musik")
        print("4. Urutkan Musik (A-Z)")
        print("5. Cari Musik berdasarkan Penyanyi")
        print("6. Keluar")

        choice = input("Pilih menu (1-6): ")

        if choice == '1':
            judul = input("Masukkan judul musik: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            genre = input("Masukkan genre musik: ")
            music = Music(judul, penyanyi, genre)
            collection.add_music(music)

        elif choice == '2':
            judul = input("Masukkan judul musik yang akan dihapus: ")
            collection.delete_music(judul)

        elif choice == '3':
            collection.display_all()

        elif choice == '4':
            collection.sort_music()

        elif choice == '5':
            penyanyi = input("Masukkan nama penyanyi: ")
            collection.search_music_by_artist(penyanyi)

        elif choice == '6':
            print("Keluar dari program. Terima kasih")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi")


if __name__ == "__main__":
    main()