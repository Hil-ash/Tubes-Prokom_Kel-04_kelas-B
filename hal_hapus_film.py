import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_hapus_film(username):
    hal_hapus_film = tk.Tk()
    hal_hapus_film.title("Sistem Pemesanan Tiket Bioskop")
    hal_hapus_film.geometry("1200x750")
    hal_hapus_film.resizable(False,False)
    hal_hapus_film.configure(bg='#000000')
    
    for i in range(5):
        hal_hapus_film.columnconfigure(i, weight=1)
    for i in range(4):
        hal_hapus_film.rowconfigure(i, weight=1)
    
    judul = tk.Label(hal_hapus_film, text="Busak Film", font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.grid(row=0,column=2 ,columnspan=2, sticky="we")

    try:
        film_data = pd.read_csv("film_data.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "File film_data.csv tidak ditemukan.")
        return
    
    image_refrence = []

    for i, row in film_data.iterrows():
        frame = tk.Frame(hal_hapus_film, bg="lightblue", width=180, height=350, relief="ridge", borderwidth=2)
        frame.grid(row=1, column=i, padx=10, sticky="we")
        frame.pack_propagate(False)

        film_judul = tk.Label(frame, text=row["judul"], font=('Georgian', 12), bg="lightblue", wraplength=160)
        film_judul.pack(pady=10)

        try:
            img = Image.open(row["gambar"])  # Pastikan gambar ada di path ini
            img = img.resize((150, 200))  # Mengubah ukuran gambar
            img_tk = ImageTk.PhotoImage(img)
            image_refrence.append(img_tk)
            img_label = tk.Label(frame, image=img_tk, bg="lightblue")
            img_label.pack(pady=10,padx=2)
        except Exception as e:
            print(f"Error loading image for {row['judul']}: {e}")

        harga = f"Rp {int(row['harga']):,}"  # Menggunakan int() untuk menghilangkan desimal dan format dengan ribuan pemisah
        harga_tiket = tk.Label(frame, text=harga, font=('Georgian', 12), bg="lightblue")
        harga_tiket.pack(pady=5)

        def tambah_film(film_judul):
            film_data = pd.read_csv("film_data.csv")
            film_data = film_data[film_data['judul'] != film_judul]
            film_data.to_csv("film_data.csv", index=False)
            try:
                kursi_data = pd.read_csv("kursi_pesanan.csv")
                kursi_data = kursi_data[kursi_data['film_judul'] != film_judul]
                kursi_data.to_csv("kursi_pesanan.csv", index=False)
                messagebox.showinfo("Success", f"Kursi yang dipesan untuk film '{film_judul}' berhasil dihapus.")
            except FileNotFoundError:
                messagebox.showerror("Error", "File kursi_pesanan.csv tidak ditemukan.")            
            hal_hapus_film.destroy()
            from hal_tambah_film import hal_tambah_film
            hal_tambah_film(username)
            
        delete_button  = tk.Button(frame, text="Busak",fg="#000000", bg="#C8102E",font=('Georgian', 8), command=lambda film_judul=row["judul"]: tambah_film(film_judul))
        delete_button.pack(pady=5)
    
    def open_hal_admin():
        from hal_admin import hal_admin
        hal_hapus_film.destroy()
        hal_admin(username)

    back_button = tk.Button(hal_hapus_film, width=8, height=1 ,text="Balek" ,fg="#000000", bg="#C8102E", font=('Georgia', 12),command=open_hal_admin)
    back_button.place(x=20, y=700 - 20 )
    
    hal_hapus_film.mainloop()
