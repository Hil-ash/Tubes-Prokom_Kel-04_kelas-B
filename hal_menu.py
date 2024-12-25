import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_menu(username):
    hal_menu = tk.Tk()
    hal_menu.title("Sistem Pemesanan Tiket Bioskop")
    hal_menu.geometry("1200x750")
    hal_menu.resizable(False,False)
    hal_menu.configure(bg='#000000')
    
    judul = tk.Label(hal_menu, text="Menu" , font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.grid(row=0,column=0, columnspan=2, sticky="we")
    
    for i in range(2):
        hal_menu.columnconfigure(i, weight=1)
    for i in range(3):
        hal_menu.rowconfigure(i, weight=1)
    
    def open_hapus_film():
        from hal_film import hal_film
        hal_menu.destroy()
        hal_film(username)
    def open_histori_pesanan():
        from hal_cancel import hal_cancel
        hal_menu.destroy()
        hal_cancel(username)
    def open_histori_pesanan_user():
        from hal_histori_user_ import hal_histori_pesanan_user
        hal_menu.destroy()
        hal_histori_pesanan_user(username)

    button_pesan = tk.Button(hal_menu, text="Pesan Tiket", width= 24, fg="#000000", bg="#C8102E", font=('Georgia', 16), command=open_hapus_film )
    button_pesan.grid(row=1, column=0)
    button_cancel = tk.Button(hal_menu, text="Cancel Tiket", width= 24, fg="#000000", bg="#C8102E", font=('Georgia', 16), command=open_histori_pesanan)
    button_cancel.grid(row=1, column=1)
    button_histori = tk.Button(hal_menu, text="Riwayat Tiket", width= 24, fg="#000000", bg="#C8102E", font=('Georgia', 16), command=open_histori_pesanan_user)
    button_histori.grid(row=2,column=0, columnspan=2)

    def open_hal_admin():
        from hal_utama import hal_Utama
        hal_menu.destroy()
        hal_Utama()
        
    back_button = tk.Button(hal_menu, width=8, height=1 ,text="balek",fg="#000000", bg="#C8102E",font=('Georgia', 12),command=open_hal_admin)
    back_button.place(x=20, y=700 - 20 )
    
    hal_menu.mainloop()
