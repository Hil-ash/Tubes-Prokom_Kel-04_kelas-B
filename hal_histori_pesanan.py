import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_histori_pesanan():
    hal_histori_pesanan = tk.Tk()
    hal_histori_pesanan.title("Sistem Pemesanan Tiket Bioskop")
    hal_histori_pesanan.geometry("1200x750")
    hal_histori_pesanan.resizable(False,False)
    hal_histori_pesanan.configure(bg='#000000')
    
    judul = tk.Label(hal_histori_pesanan, text="Riwayat Pesanan", fg="#C8102E",bg="#000000",font=('Georgian', 30))
    judul.pack(pady=15)
    
    def load_pesanan_data():
        try:
            # Membaca data dari file CSV
            histori_data = pd.read_csv("pesanan_data.csv")
            return histori_data
        except FileNotFoundError:
            messagebox.showerror("Error", "File pesanan_data.csv tidak ditemukan.")
    
    def show_pesanan_data(tree):
    # Menghapus semua item yang ada di Treeview
        for item in tree.get_children():
            tree.delete(item)  # Menggunakan tree.delete() untuk menghapus item

    # Memuat data histori pemesanan
        histori_data = load_pesanan_data()

        if histori_data is not None:  # Pastikan histori_data tidak None
            # Menambahkan data ke Treeview
            for index, row in histori_data.iterrows():
                tree.insert("", "end", values=(row["film_judul"], row["jumlah_kursi"], row["kode_kursi"], row["username"]))
    
    frame = tk.Frame(hal_histori_pesanan, bg="lightblue")
    frame.pack(pady=20)
    
    columns = ("Film", "Jumlah Kursi", "Kode Kursi", "Username")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    tree.pack(side="left")
    
    # Mengatur lebar kolom
    tree.column("Film", width=150)
    tree.column("Jumlah Kursi", width=100)
    tree.column("Kode Kursi", width=100)
    tree.column("Username", width=100)

    # Mengatur header kolom
    tree.heading("Film", text="Film")
    tree.heading("Jumlah Kursi", text="Jumlah Kursi")
    tree.heading("Kode Kursi", text="Kode Kursi")
    tree.heading("Username", text="Username")
    
    # Menampilkan histori pemesanan
    show_pesanan_data(tree)
    
    # Menambahkan scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscroll=scrollbar.set)        

    def open_hal_admin():
        hal_histori_pesanan.destroy()
        from hal_admin import hal_admin
        hal_admin()

    back_button = tk.Button(hal_histori_pesanan, width=8, height=1 ,text="balek", fg="#000000", bg="#C8102E", font=('Georgia', 12),command=open_hal_admin)
    back_button.place(x=20, y=700 - 20 )
        
    hal_histori_pesanan.mainloop()