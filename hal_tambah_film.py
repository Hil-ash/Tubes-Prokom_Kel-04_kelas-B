import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_tambah_film(username):
    hal_tambah_film = tk.Tk()
    hal_tambah_film.title("Sistem Pemesanan Tiket Bioskop")
    hal_tambah_film.geometry("1200x750")
    hal_tambah_film.resizable(False,False)
    hal_tambah_film.configure(bg='#000000')
    
    for i in range(3):
        hal_tambah_film.columnconfigure(i, weight=1)
    for i in range(4):
        hal_tambah_film.rowconfigure(i, weight=1)
    
    judul = tk.Label(hal_tambah_film, text="Tambah Film Anyar", font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.grid(row=0,column=0 ,columnspan=3, sticky="we")
    
    frame1 = tk.Frame(hal_tambah_film, bg="lightblue", width=300, height=200)
    frame1.grid(row=1, column=1, padx=10)
    frame1.pack_propagate(False)
    
    subjudul= tk.Label(frame1, text="Film Anyar", fg="#C8102E",bg="lightblue",font=('Georgian', 18))
    subjudul.pack(pady=10,padx=2)
    tk.Label(frame1, text="Jeneng Film",fg="#000000",font=('Georgian', 15), bg="lightblue").pack(pady=5)
    entry_nama_film = tk.Entry(frame1)
    entry_nama_film.pack(pady=5)
    tk.Label(frame1, text="Rego",fg="#000000",font=('Georgian', 15), bg="lightblue").pack(pady=5)
    entry_harga = tk.Entry(frame1)
    entry_harga.pack(pady=5)
        
    def pilih_gambar():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if file_path:
            gambar_path.set(file_path)
    
    gambar_path = tk.StringVar()
    tk.Button(frame1, text="Pilih Gambar",fg="#000000", bg="#C8102E",font=('Georgian', 12), command=pilih_gambar).pack(pady=5)
    
    def tambahkan_film():
        nama_film = entry_nama_film.get()
        harga = entry_harga.get()
        gambar = gambar_path.get()

        new_film = pd.DataFrame({'judul': [nama_film], 'harga': [harga], 'gambar': [gambar]})
        new_film.to_csv("film_data.csv", mode='a', header=False, index=False)
        messagebox.showinfo("Success", f"Film '{nama_film}' berhasil ditambahkan.")
        hal_tambah_film.destroy()
        from hal_admin import hal_admin
        hal_admin(username)
        
    button_tambah = tk.Button(hal_tambah_film, text="Tambahkan",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=tambahkan_film)
    button_tambah.grid(row=2, column=1)
    
    hal_tambah_film.mainloop()
