import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_reset_kursi():
    hal_reset_kursi = tk.Tk()
    hal_reset_kursi.title("Sistem Pemesanan Tiket Bioskop")
    hal_reset_kursi.geometry("1200x750")
    hal_reset_kursi.resizable(False,False)
    hal_reset_kursi.configure(bg='#000000')
    
    for i in range(5):
        hal_reset_kursi.columnconfigure(i, weight=1)
    for i in range(4):
        hal_reset_kursi.rowconfigure(i, weight=1)
    
    judul = tk.Label(hal_reset_kursi, text="Reset Film", font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.grid(row=0,column=2 ,columnspan=2, sticky="we")
    
    # Membaca data film dari file CSV
    try:
        film_data = pd.read_csv("film_data.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "File film_data.csv tidak ditemukan.")
        return
    
    image_refrence = []

    # Loop untuk membuat frame
    for i, row in film_data.iterrows():
        frame = tk.Frame(hal_reset_kursi, bg="lightblue", width=180, height=350, relief="ridge", borderwidth=2)
        frame.grid(row=1, column=i, padx=10, sticky="we")
        frame.pack_propagate(False)

        # Judul Film
        film_judul = tk.Label(frame, text=row["judul"], font=('Georgian', 15), bg="lightblue", wraplength=160)
        film_judul.pack(pady=10)

        # Gambar Film
        try:
            img = Image.open(row["gambar"])  # Pastikan gambar ada di path ini
            img = img.resize((150, 200))  # Mengubah ukuran gambar
            img_tk = ImageTk.PhotoImage(img)
            image_refrence.append(img_tk)
            img_label = tk.Label(frame, image=img_tk, bg="lightblue")
            img_label.pack(pady=10,padx=2)
        except Exception as e:
            print(f"Error loading image for {row['judul']}: {e}")

        # Harga Tiket
        harga = f"Rp {int(row['harga']):,}"  # Menggunakan int() untuk menghilangkan desimal dan format dengan ribuan pemisah
        harga_tiket = tk.Label(frame, text=harga, font=('Georgian', 16), bg="lightblue")
        harga_tiket.pack(pady=5)
        
    frame1 = tk.Frame(hal_reset_kursi, bg="lightblue", width=180, height=50)
    frame1.grid(row=2, column=2,columnspan=2, padx=10, sticky="we")
    
    isi = tk.Label(frame1, text="Pilih Film Seng pingin direset", font=('Georgian', 15), bg="lightblue")
    isi.pack(pady=10,padx=2)
    
    hps_film = tk.Entry(frame1, font=('Georgian', 10), bg="lightblue")
    hps_film.pack(pady=10,padx=2)
    
    def reset_film():
        judul = hps_film.get()
        if judul == "":
            messagebox.showinfo("Error","Masukkan judul film yang ingin direset")
        
        with open("kursi_pesanan.csv","r") as file:
            lines = file.readlines()
            
        with open("kursi_pesanan.csv", "w") as file:
            for line in lines:
                if not line.startswith(judul + ","):
                    file.write(line)
        messagebox.showinfo("Informasi", f"Kursi untuk film '{judul}' telah direset.")
        hal_reset_kursi.destroy()
        from hal_admin import hal_admin
        hal_admin()
    
    def reset_semua():
        try:
            with open("kursi_pesanan.csv", "r") as file:
                lines = file.readline()
                header = lines[0]
                data_lines = lines[1:]
            with open("kursi_pesanan.csv", "w") as file:
                file.write(header)
                for line in data_lines:
                    file.write(line)
            messagebox.showinfo("Informasi", "Semua pesanan kursi telah dihapus.")
            hal_reset_kursi.destroy()
            from hal_admin import hal_admin
            hal_admin()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menghapus pesanan: {e}") 
    
    button2 = tk.Button(frame1, text="Hapus",bg="#C8102E", fg="#000000", command=reset_film)
    button2.pack(pady=10,padx=2)    
    
    button3 = tk.Button(frame1, text="Hapus Semua",bg="#C8102E", fg="#000000", command=reset_semua)
    button3.pack(pady=10,padx=2)   

    def open_hal_admin():
        from hal_admin import hal_admin
        hal_reset_kursi.destroy()
        hal_admin()

    back_button = tk.Button(hal_reset_kursi, width=8, height=1 ,text="Balek" ,font=('Georgia', 12), bg="#C8102E", fg="#000000",command=open_hal_admin)
    back_button.place(x=20, y=700 - 20 )
    
    hal_reset_kursi.mainloop()