import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re

def hal_cancel(username):
    hal_cancel = tk.Tk()
    hal_cancel.title("Cancel Tiket")
    hal_cancel.geometry("1200x750")
    hal_cancel.resizable(False, False)
    hal_cancel.configure(bg='#000000')
    
    for i in range(6):
        hal_cancel.columnconfigure(i, weight=1)
    for i in range(4):
        hal_cancel.rowconfigure(i, weight=1)
    
    judul = tk.Label(hal_cancel, text="Pilih Seng Meh dicancel", font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.grid(row=0, column=0, columnspan=6, sticky="we")

    try:
        pesanan_data = pd.read_csv("pesanan_data.csv")  # File CSV yang berisi data pesanan
    except FileNotFoundError:
        messagebox.showerror("Error", "File pesanan_data.csv tidak ditemukan.")
        return
    user_pesanan = pesanan_data[pesanan_data['username'] == username]
    if user_pesanan.empty:
        messagebox.showinfo("Info", "Anda tidak memiliki pesanan yang dapat dibatalkan.")
        hal_cancel.destroy()
        from hal_menu import hal_menu
        hal_menu(username)
        return

    for frame_count, row in user_pesanan.iterrows():
        column = frame_count % 6
        rows = frame_count // 4
        frame = tk.Frame(hal_cancel, bg="lightblue", relief="ridge", borderwidth=2)
        frame.grid(row=rows+1, column=column, padx=5)

        struk_text = f"{'Nama Film':<20}: {row['film_judul']}\n"
        struk_text += f"{'Jumlah Kursi':<20}: {row['jumlah_kursi']}\n"
        struk_text += f"{'Kode Kursi':<20}: {row['kode_kursi']}\n"
        
        info_label = tk.Label(frame, text=struk_text, font=('Georgia', 12) , bg="lightblue", justify="left")
        info_label.pack(pady=5,padx=2)

        def batalkan_pesanan(film_judul, kode_kursi):
            kode_list = [kode.strip() for kode in re.split(r';', kode_kursi)]
            print(f"Kode kursi yang akan dihapus: {kode_list}")


            with open("pesanan_data.csv", "r") as file:
                pesanan_lines = file.readlines()

            with open("pesanan_data.csv", "w") as file:
                found = False  # Untuk memastikan kita hanya menghapus satu baris
                for line in pesanan_lines:
                    if not found and kode_kursi in line:
                        found = True  # Tandai bahwa kita sudah menghapus satu baris
                        continue  # Lewati baris ini
                    file.write(line)  # Tulis baris yang tidak dihapus

            with open("kursi_pesanan.csv", "r") as file:
                lines = file.readlines()

            with open("kursi_pesanan.csv", "w") as file:
                for line in lines:
                    print(f"Memeriksa baris: {line.strip()}")
                    if not (line.startswith(film_judul + ",") and any(kode in line for kode in kode_list)):
                        file.write(line)  # Tulis baris yang tidak dihapus
                    else:
                        print(f"Baris dihapus: {line.strip()}")
            hal_cancel.destroy()
            from hal_menu import hal_menu
            hal_menu(username)

        cancel_button = tk.Button(frame, text="Cancel Tiket", width=20,fg="#000000", bg="#C8102E", font=('Georgia', 8),
                                  command=lambda film_judul=row['film_judul'], kode_kursi=row['kode_kursi']: batalkan_pesanan(film_judul, kode_kursi))
        cancel_button.pack(pady=5)
        
    def open_hal_sign_in():
        from hal_menu import hal_menu
        hal_cancel.destroy()
        hal_menu(username)
        
    back_button = tk.Button(hal_cancel, width=8, height=1 ,text="Balek" ,fg="#000000", bg="#C8102E", font=('Georgia', 12), command=open_hal_sign_in)
    back_button.place(x=20, y=700 - 20 )

    hal_cancel.mainloop()
