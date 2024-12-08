import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re


def hal_penutup(username):
    hal_penutup = tk.Tk()
    hal_penutup.title("Sistem Pemesanan Tiket Bioskop")
    hal_penutup.geometry("1200x750")
    hal_penutup.resizable(False,False)
    hal_penutup.configure(bg='#000000')
    
    pembatas = "=" * 37
    judul = "Bioskop CGV"
        
    penutup = f"{pembatas}\n{judul}\n{pembatas}\n"
    penutup += f"Cetak Tiket\n"
    penutup += f"Tiket telah dicetak, silahkan ambil pada file txt\n"
    penutup += f" \n"
    penutup += f"Terima kasih telah memesan tiket\n"
    penutup += f"Selamat menonton\n"
    penutup += f"{pembatas}\n"

    frame = tk.Frame(hal_penutup, bg="lightblue")
    frame.pack(expand=True)
    judul = tk.Label(frame, text=penutup , font=('Georgia', 34), fg="#C8102E", bg="lightblue", justify="center")
    judul.pack(pady= 10, padx= 10)
    
    def pesan_lagi():
        from hal_menu import hal_menu
        hal_penutup.destroy()
        hal_menu(username)
    
    def keluar():
        hal_penutup.destroy()
    
    pesan_lagi_1 = tk.Button(hal_penutup,width=24, text="Pesan meneh",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=pesan_lagi)
    pesan_lagi_1.pack(padx=50, pady=10)
    
    keluar_button = tk.Button(hal_penutup,width=24, text="Metu",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=keluar)
    keluar_button.pack(padx= 50, pady= 10)
    
    hal_penutup.mainloop()