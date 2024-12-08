import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re


def hal_Sigh_Up():
   hal_Sigh_Up = tk.Tk()
   hal_Sigh_Up.title("Sistem Pemesanan Tiket Bioskop")
   hal_Sigh_Up.geometry("1200x750")
   hal_Sigh_Up.resizable(False,False)
   hal_Sigh_Up.configure(bg='#000000')
   
   judul = tk.Label(hal_Sigh_Up, text="Gawe Akun Sek" , font=('Georgia', 34), fg="#C8102E", bg="#000000")
   judul.pack(padx= 20 , pady= 100)
   
   frame = tk.Frame(hal_Sigh_Up, bg="#000000", width=500, height=300, relief="ridge", borderwidth=0)
   frame.pack(padx= 50, pady=10)
   frame.pack_propagate(False)
   
   tk.Label(frame, text="Username", fg="#C8102E", bg="#000000", font=('Georgia', 16)).pack(padx=50, pady=10, fill=tk.X, expand=True)
   isi_username = tk.Entry(frame)
   isi_username.pack(padx=50, pady=10, fill=tk.X, expand=True)
   
   tk.Label(frame, text="Password", fg="#C8102E", bg="#000000", font=('Georgia', 16)).pack(padx=50, pady=10, fill=tk.X, expand=True)
   isi_password = tk.Entry(frame, show="*")
   isi_password.pack(padx=50, pady=10, fill=tk.X, expand=True)
   
   def Sign_up ():
       A1 = isi_username.get()
       A2 = isi_password.get()
       
       if A1=="" or A2=="":
           messagebox.showinfo("Eror","isi semuanya")
       else :
           with open("user_data.csv", "a") as file:
               file.write("\n"+A1+","+A2)
           messagebox.showinfo("Informasi","Pembuatan berhasil")
           hal_Sigh_Up.destroy()
           from hal_utama import hal_Utama
           hal_Utama()

   hal_Sigh_Up.bind('<Return>', lambda event: Sign_up())
   
   sign_up_button = tk.Button(frame, width=20 ,text="Gawe" ,fg="#000000", bg="#C8102E", font=('Georgia', 16), command= Sign_up)
   sign_up_button.pack(padx=50 , pady=40)
   
   def open_hal_Utama():
       from hal_utama import hal_Utama
       hal_Sigh_Up.destroy()
       hal_Utama()
    
   back_button = tk.Button(hal_Sigh_Up, width=8, height=1 ,text="Balek" ,fg="#000000", bg="#C8102E", font=('Georgia', 12), command= open_hal_Utama)
   back_button.place(x=20, y=700 - 20 )
   
   hal_Sigh_Up.mainloop()
