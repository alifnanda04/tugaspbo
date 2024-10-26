class Pesanan:
    def __init__(self, ID: int, nama: str, detail: str):
        self.set_pesanan(ID, nama, detail)

    def set_pesanan(self, ID: int, nama: str, detail: str):
        if ID <= 0:
            raise ValueError("ID harus merupakan bilangan bulat positif.")
        if not nama or not detail:
            raise ValueError("Nama dan detail tidak boleh kosong.")
        
        self.ID = ID
        self.nama = nama
        self.detail = detail

    def __str__(self):
        return f"Pesanan[ID: {self.ID}, Nama: {self.nama}, Detail: {self.detail}]"


class Pengiriman:
    def __init__(self, id: int, nama: str, informasi: str, tanggal: str, alamat: str):
        self.set_pengiriman(id, nama, informasi, tanggal, alamat)

    def set_pengiriman(self, id: int, nama: str, informasi: str, tanggal: str, alamat: str):
        if id <= 0:
            raise ValueError("ID harus merupakan bilangan bulat positif.")
        if not nama or not alamat:
            raise ValueError("Nama dan alamat tidak boleh kosong.")
        
        self.id = id
        self.nama = nama
        self.informasi = informasi
        self.tanggal = tanggal
        self.alamat = alamat

    def proses_pengiriman(self):
        print(f"Mengolah pengiriman untuk {self.nama} ke alamat {self.alamat} pada {self.tanggal}.")

    def __str__(self):
        return (f"Pengiriman[ID: {self.id}, Nama: {self.nama}, "
                f"Informasi: {self.informasi}, Tanggal: {self.tanggal}, Alamat: {self.alamat}]")

def menu():
    print("\nMenu:")
    print("1. Buat Pesanan")
    print("2. Perbarui Pesanan")
    print("3. Proses Pengiriman")
    print("4. Tampilkan Informasi Semua Pesanan dan Pengiriman")
    print("5. Keluar")

def main():
    pesanan_list = [] 
    pengiriman = None

    while True:
        menu()
        pilihan = input("Pilih opsi (1-5): ")

        try:
            if pilihan == '1':
                ID = int(input("Masukkan ID Pesanan: "))
                nama = input("Masukkan Nama Item: ")
                detail = input("Masukkan Detail Item: ")
                pesanan = Pesanan(ID, nama, detail)
                pesanan_list.append(pesanan)
                print("Pesanan berhasil dibuat.")

            elif pilihan == '2':
                if pesanan_list:
                    ID = int(input("Masukkan ID Pesanan yang akan diperbarui: "))
                    pesanan = next((p for p in pesanan_list if p.ID == ID), None)
                    if pesanan:
                        nama = input("Masukkan Nama Item baru: ")
                        detail = input("Masukkan Detail Item baru: ")
                        pesanan.set_pesanan(ID, nama, detail)
                        print("Pesanan berhasil diperbarui.")
                    else:
                        print("Pesanan tidak ditemukan.")
                else:
                    print("Belum ada pesanan dibuat.")

            elif pilihan == '3':
                if pesanan_list:
                    id = int(input("Masukkan ID Pengiriman: "))
                    nama = input("Masukkan Nama Penerima: ")
                    informasi = input("Masukkan Informasi Pengiriman: ")
                    tanggal = input("Masukkan Tanggal Pengiriman (YYYY-MM-DD): ")
                    alamat = input("Masukkan Alamat Pengiriman: ")
                    pengiriman = Pengiriman(id, nama, informasi, tanggal, alamat)
                    pengiriman.proses_pengiriman()
                else:
                    print("Belum ada pesanan dibuat.")

            elif pilihan == '4':
                if pesanan_list:
                    print("\nSemua Pesanan:")
                    for p in pesanan_list:
                        print(p)
                else:
                    print("Belum ada pesanan dibuat.")
                
                if pengiriman:
                    print("\nPengiriman Terakhir:")
                    print(pengiriman)
                else:
                    print("Pengiriman belum dibuat")

            elif pilihan == '5':
                print("Keluar dari program")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih antara 1-5.")

        except ValueError as e:
            print(f"Kesalahan: {e}")

if __name__ == "__main__":
    main()
