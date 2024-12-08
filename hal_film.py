import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_film(username):
    hal_film = tk.Tk()
    hal_film.title("Sistem Pemesanan Tiket Bioskop")
    hal_film.geometry("1200x750")
    hal_film.resizable(False,False)
    hal_film.configure(bg='#000000')
    
    for i in range(5):
        hal_film.columnconfigure(i, weight=1)
    for i in range(4):
        hal_film.rowconfigure(i, weight=1)
    
    judul = tk.Label(hal_film, text="Pilih Film", fg="#C8102E", bg="#000000",font=('Georgia', 30))
    judul.grid(row=0,column=2 ,columnspan=2, sticky="we")

    try:
        film_data = pd.read_csv("film_data.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "File film_data.csv tidak ditemukan.")
        return
    
    image_refrence =[]
    for i, row in film_data.iterrows():
        frame = tk.Frame(hal_film, bg="#FFD700", width=180, height=350, relief="ridge", borderwidth=2)
        frame.grid(row=1, column=i, padx=10, sticky="we")
        frame.pack_propagate(False)

        film_judul = tk.Label(frame, text=row["judul"], font=('Arial', 15), bg="#FFD700", wraplength=160)
        film_judul.pack(pady=10)

        try:
            img = Image.open(row["gambar"])  # Pastikan gambar ada di path ini
            img = img.resize((150, 200))  # Mengubah ukuran gambar
            img_tk = ImageTk.PhotoImage(img)
            image_refrence.append(img_tk)
            img_label = tk.Label(frame, image=img_tk, bg="#FFD700")
            #img_label.image = img_tk
            img_label.pack(pady=10,padx=2)
        except Exception as e:
            print(f"Error loading image for {row['judul']}: {e}")

        # Harga Tiket
        harga = f"Rp {int(row['harga']):,}"  # Menggunakan int() untuk menghilangkan desimal dan format dengan ribuan pemisah
        harga_tiket = tk.Label(frame, text=harga, font=('Arial', 15), bg="#FFD700")
        harga_tiket.pack(pady=5)
        
        def open_hal_kursi(film_judul):
            from hal_kursi import hal_kursi
            hal_film.destroy()
            hal_kursi(film_judul,username)
        
        button1 = tk.Button(hal_film, width=8, height=1 ,text="Pilih" ,fg="#000000", bg="#C8102E",font=('Georgia', 10),
                            command=lambda film_judul=row["judul"]: open_hal_kursi(film_judul))
        button1.grid(row= 2, column=i)
        
    def open_hal_sign_in():
        from hal_menu import hal_menu
        hal_film.destroy()
        hal_menu()
        
    back_button = tk.Button(hal_film, width=8, height=1 ,text="Balek" ,fg="#000000", bg="#C8102E",font=('Georgia', 12),command=open_hal_sign_in)
    back_button.place(x=20, y=700 - 20 )
    
    hal_film.mainloop()