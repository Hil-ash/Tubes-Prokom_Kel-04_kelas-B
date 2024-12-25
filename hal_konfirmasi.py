import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re
from datetime import datetime

def hal_konfirmasi(film_judul, pilihan_kursi, harga_tiket, username):
    hal_konfirmasi = tk.Tk()
    hal_konfirmasi.title("Sistem Pemesanan Tiket Bioskop")
    hal_konfirmasi.geometry("1200x750")
    hal_konfirmasi.resizable(False,False)
    hal_konfirmasi.configure(bg='#000000')
    
    judul = tk.Label(hal_konfirmasi, text="Konfirmasi Pesanan" , font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.pack(padx= 20 , pady= 20)
    
    max_length = max(len(username), len(film_judul), len(', '.join(pilihan_kursi)), len(f"Rp {harga_tiket:,}"))
    pembatas = "=" * (max_length+17)
    struk_text = f"{pembatas}\n         Tiket Bioskop          \n{pembatas}\n"
    # Menampilkan informasi pemesanan
    jumlah_kursi = len(pilihan_kursi)
    total_harga = jumlah_kursi*harga_tiket

    struk_text += f"{'Nama Pengguna':<20}: {username}\n"
    struk_text += f"{'Nama Film':<20}: {film_judul}\n"
    struk_text += f"{'Jumlah Kursi':<20}: {jumlah_kursi}\n"
    struk_text += f"{'Kode Kursi':<20}: {', '.join(pilihan_kursi)}\n"
    struk_text += f"{'Total Harga':<20}: Rp {total_harga:,}\n"
    struk_text += f"{pembatas}\n"

    struk_label = tk.Label(hal_konfirmasi, text=struk_text, font=('georgia',20), bg="lightblue", justify="left")
    struk_label.pack(expand=True)
    
    def batalkan_pesanan():
        # Hapus kursi yang dipilih dari file
        with open("kursi_pesanan.csv", "r") as file:
            lines = file.readlines()

        with open("kursi_pesanan.csv", "w") as file:
            for line in lines:
                if not any(kursi in line for kursi in pilihan_kursi):
                    file.write(line)    
        hal_konfirmasi.destroy()
        from hal_film import hal_film
        hal_film(username)
    
    def konfirmasi_pesanan(film_judul, pilihan_kursi, username):
        # Hitung jumlah kursi
            jumlah_kursi = len(pilihan_kursi)
            kode_kursi = '; '.join(pilihan_kursi)  # Menggabungkan kode kursi menjadi satu string
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            data_to_save = f"{film_judul},{jumlah_kursi},{kode_kursi},{username},{waktu}\n"

            with open("pesanan_data.csv", 'a') as file:  # 'a' mode untuk menambah data
                file.write(data_to_save)  # Tulis data pesanan
            with open("tiket.txt", "a+") as file:
                file.write(struk_text)
            
            hal_konfirmasi.destroy()
            from hal_penutup import hal_penutup
            hal_penutup(username)

    konfirmasi_button = tk.Button(hal_konfirmasi,width=24, text="Konfirmasi Pesanan",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=lambda :konfirmasi_pesanan(film_judul, pilihan_kursi, username))
    konfirmasi_button.pack(padx=50, pady=10)
    
    cancel_button = tk.Button(hal_konfirmasi,width=24, text="Batalkan Pesanan",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=batalkan_pesanan)
    cancel_button.pack(padx= 50, pady= 10)

    hal_konfirmasi.mainloop()
