import tkinter as tk
from tkinter import ttk, messagebox

class ClothingStoreApp:
    def __init__(self, root):  # Menggunakan __init__
        self.root = root
        self.root.title("Aplikasi Pemesanan Toko Baju")
        self.root.geometry("500x400")
        
        self.orders = []  # List untuk menyimpan pesanan
        
        self.create_widgets()
        
    def create_widgets(self):
        # Judul Aplikasi
        title_label = tk.Label(self.root, text="Aplikasi Pemesanan Toko Baju", font=("Arial", 16))
        title_label.pack(pady=10)
        
        # Nama Pemesan
        name_label = tk.Label(self.root, text="Nama Pemesan:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root, width=35)
        self.name_entry.pack(pady=5)
        
        # Pilihan Baju
        clothing_label = tk.Label(self.root, text="Pilihan Baju:")
        clothing_label.pack()
        self.clothing_option = ttk.Combobox(self.root, values=("Kemeja", "Kaos", "Jaket", "Celana"))
        self.clothing_option.pack(pady=5)
        
        # Jumlah Pesanan
        quantity_label = tk.Label(self.root, text="Jumlah Pesanan:")
        quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root, width=10)
        self.quantity_entry.pack(pady=5)
        
        # Tombol untuk mengirim pesanan
        submit_button = tk.Button(self.root, text="Pesan", command=self.submit_order)
        submit_button.pack(pady=20)
        
        # Tombol untuk menghapus pesanan
        delete_button = tk.Button(self.root, text="Hapus Pesanan", command=self.delete_order)
        delete_button.pack(pady=5)
        
        # Tombol untuk menghapus semua pesanan
        delete_all_button = tk.Button(self.root, text="Hapus Semua Pesanan", command=self.delete_all_orders)
        delete_all_button.pack(pady=5)
        
        # Tabel Daftar Pesanan
        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.order_tree = ttk.Treeview(frame, columns=("Nama", "Baju", "Jumlah"), show='headings')
        self.order_tree.heading("Nama", text="Nama Pemesan")
        self.order_tree.heading("Baju", text="Pilihan Baju")
        self.order_tree.heading("Jumlah", text="Jumlah Pesanan")
        self.order_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar untuk tabel
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.order_tree.yview)
        self.order_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def submit_order(self):
        name = self.name_entry.get().strip()
        clothing = self.clothing_option.get()
        quantity = self.quantity_entry.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Nama Pemesan tidak boleh kosong!")
            return
        
        if not clothing:
            messagebox.showerror("Error", "Silakan pilih baju!")
            return
        
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Jumlah pesanan harus berupa angka positif!")
            return
        
        # Menambahkan pesanan ke daftar
        self.orders.append((name, clothing, quantity))
        self.update_order_table()
        
        # Menghapus input setelah pengiriman
        self.name_entry.delete(0, tk.END)
        self.clothing_option.set('')
        self.quantity_entry.delete(0, tk.END)

    def update_order_table(self):
        # Menghapus semua item di tabel
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)
        
        # Menambahkan semua pesanan ke tabel
        for order in self.orders:
            self.order_tree.insert("", "end", values=order)

    def delete_order(self):
        selected_item = self.order_tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Silakan pilih pesanan yang ingin dihapus!")
            return
        
        # Menghapus pesanan dari daftar
        for item in selected_item:
            index = self.order_tree.index(item)
            del self.orders[index]
            self.order_tree.delete(item)
        
        self.update_order_table()

    def delete_all_orders(self):
        self.orders.clear()
        self.update_order_table()
        messagebox.showinfo("Informasi", "Semua pesanan berhasil dihapus!")

if __name__ == "__main__":  # Menggunakan __main__
    root = tk.Tk()
    app = ClothingStoreApp(root)
    root.mainloop()
