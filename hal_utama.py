import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re


def hal_Utama ():
    hal_Utama = tk.Tk()
    hal_Utama.title("Sistem Pemesanan Tiket Bioskop")
    hal_Utama.geometry("1200x750")
    hal_Utama.resizable(False,False)
    hal_Utama.configure(bg='#000000')
    
    def open_sign_in():
        from hal_sigh_in import hal_Sigh_in
        hal_Utama.destroy()
        hal_Sigh_in()
        
    def open_sign_up():
        from hal_sigh_up import hal_Sigh_Up
        hal_Utama.destroy()
        hal_Sigh_Up()
    
    judul = tk.Label(hal_Utama, text="Selamat Datang di CGV" , font=('Georgia', 40, "bold"), fg=("#C8102E"), bg="#000000")
    judul.pack(padx= 20 , pady= 70)
    
    frame = tk.Frame(hal_Utama, bg="#000000", width=300, height=200, relief="ridge", borderwidth=0)
    frame.pack(padx= 50, pady=100)
    frame.pack_propagate(False)
    
    button_sign_in = tk.Button(frame, width=28, text="Sign In", fg="#000000", bg="#C8102E", font=('Georgia', 16), command=open_sign_in)
    button_sign_in.pack(padx=50 , pady=40)
    button_sign_up = tk.Button(frame, width=28, text="Sign Up", fg="#000000", bg="#C8102E", font=('Georgia', 16), command=open_sign_up)
    button_sign_up.pack(padx=50 , pady=5)
    
    def exit():
        hal_Utama.destroy()
    
    button_exit = tk.Button(hal_Utama, width=8, height=1 ,text="Metu" , fg="#000000", bg="#C8102E",font=('Georgia', 12), command=exit)
    button_exit.place(x=20, y=700 - 20 )
    
    hal_Utama.mainloop()
