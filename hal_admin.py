import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_admin(username):
    hal_admin = tk.Tk()
    hal_admin.title("Sistem Pemesanan Tiket Bioskop")
    hal_admin.geometry("1200x750")
    hal_admin.resizable(False,False)
    hal_admin.configure(bg='#000000')
    
    judul = tk.Label(hal_admin, text="Punya Admin" , fg="#C8102E", bg="#000000", font=('Georgian', 34))
    judul.grid(row=0,column=0, columnspan=2, sticky="we")
    
    for i in range(2):
        hal_admin.columnconfigure(i, weight=1)
    for i in range(4):
        hal_admin.rowconfigure(i, weight=1)
    
    def open_hapus_film():
        from hal_hapus_film import hal_hapus_film
        hal_admin.destroy()
        hal_hapus_film(username)
    def open_histori_pesanan():
        from hal_histori_pesanan import hal_histori_pesanan
        hal_admin.destroy()
        hal_histori_pesanan(username)
    def open_reset_kursi():
        from hal_reset_kursi import hal_reset_kursi
        hal_admin.destroy()
        hal_reset_kursi(username)
    def open_cek():
        from hal_film import hal_film
        hal_admin.destroy()
        hal_film(username)
        
    button_hapus_film = tk.Button(hal_admin, text="Hapus Film", width= 20, fg="#000000", bg="#C8102E",font=('Georgian', 16), command=open_hapus_film )
    button_hapus_film.grid(row=1, column=0)
    button_histori_pesanan = tk.Button(hal_admin, text="Histori Pemesanan", width= 20, fg="#000000", bg="#C8102E",font=('Georgian', 16), command=open_histori_pesanan)
    button_histori_pesanan.grid(row=1, column=1)
    button_reset_kursi = tk.Button(hal_admin, text="Reset Kursi", width= 20, fg="#000000", bg="#C8102E",font=('Georgian', 16), command=open_reset_kursi)
    button_reset_kursi.grid(row=2, column=0)
    button_cek = tk.Button(hal_admin, text="cek",width= 20, fg="#000000", bg="#C8102E",font=('Georgian', 16),command=open_cek)
    button_cek.grid(row=2, column=1)

    hal_admin.mainloop()
