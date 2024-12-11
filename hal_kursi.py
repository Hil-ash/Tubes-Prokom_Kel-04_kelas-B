import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import re


def hal_kursi(film_judul,username):
    hal_kursi = tk.Tk()
    hal_kursi.title("Sistem Pemesanan Tiket Bioskop")
    hal_kursi.geometry("1200x750")  # Ukuran jendela disesuaikan untuk menampung 6 frame
    hal_kursi.resizable(False, False)
    hal_kursi.configure(bg='#000000')
    
    # Memuat kursi yang sudah dipesan dari file CSV
    kursi_dipesan = set()
    try:
        with open("kursi_pesanan.csv", "r") as file:
            for line in file:
                try :
                    film, kursi = line.strip().split(",")
                    if film == film_judul:  # Hanya ambil kursi yang dipesan untuk film ini
                        kursi_dipesan.add(kursi)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        pass

    for i in range(3):
        hal_kursi.columnconfigure(i, weight=1)
    for i in range(5):
        hal_kursi.rowconfigure(i, weight=1)
    
    judul = tk.Label(hal_kursi, text=f"Pilih kursi untuk {film_judul}" , font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.grid(row=0, column=0, columnspan=3)
    
    frame = tk.Frame(hal_kursi, bg="lightblue", width=500, height=300, relief="ridge", borderwidth=2)
    frame.grid(row=1,column=0, columnspan=3, sticky="we", padx=20)
    frame.pack_propagate(False)
    
    for i in range(3):
        frame.columnconfigure(i, weight=1)
    for i in range(3):
        frame.rowconfigure(i, weight=1)
    
    frame1= tk.Frame(frame, width=200, height=100,relief="ridge", borderwidth=2)
    frame1.grid(column=1,row=0, pady=20, sticky="we")
    frame1.pack_propagate(False)
    
    frame2= tk.Frame(frame, width=370, height=250,relief="ridge", borderwidth=2)
    frame2.grid(column=0,row=2, pady=20)
    frame2.pack_propagate(False)
    
    frame3= tk.Frame(frame, width=370, height=250,relief="ridge", borderwidth=2)
    frame3.grid(column=1,row=2, pady=20)
    frame3.pack_propagate(False)
    
    frame4= tk.Frame(frame, width=370, height=250,relief="ridge", borderwidth=2)
    frame4.grid(column=2,row=2, pady=20)
    frame4.pack_propagate(False)
    
    layout_kursi = [
        [[1] * 5 for _ in range(4)],  # Frame 1
        [[1] * 5 for _ in range(4)],  # Frame 2
        [[1] * 5 for _ in range(4)],  # Frame 3
    ]

    buttons = []  # Menyimpan referensi tombol
    pilihan_kursi = []  # Menyimpan kursi yang dipilih
    jumlah_kolom = 5

    def pilih_kursi(frame_index, row, col):
        if layout_kursi[frame_index][row][col] == 1:  # Jika kursi tersedia
            layout_kursi[frame_index][row][col] = 0  # Tandai kursi sebagai terisi
            buttons[frame_index][row][col].config(bg="red", state="disabled")
            kursi_nomor = row * jumlah_kolom + col + 1
            pilihan_kursi.append(chr(65 + frame_index) + str(kursi_nomor))  # Simpan pilihan kursi  

    # Membuat grid kursi untuk frame 2 dan frame 3 dengan logika yang sama
    for frame_index in range(3):
        row_buttons = []
        for row in range(4):
            row_buttons.append([])
            for col in range(jumlah_kolom):
                kursi_nomor = row * jumlah_kolom + col + 1
                kursi_label = chr(65 + frame_index) + str(kursi_nomor)  # Menghasilkan label seperti A1, A2, B1, dll.
                kursi = tk.Button(eval(f'frame{frame_index + 2}'), text=kursi_label, width=5, height=2,
                                    bg="green" if kursi_label not in kursi_dipesan else "red",
                                    state=tk.NORMAL if kursi_label not in kursi_dipesan else tk.DISABLED,
                                    command=lambda r=row, c=col, fi=frame_index: pilih_kursi(fi, r, c))
                kursi.grid(row=row, column=col, padx=5, pady=5)
                row_buttons[-1].append(kursi)
        buttons.append(row_buttons)

    def reset_kursi():
        # Reset layout untuk semua frame
        for frame_index, layout in enumerate(layout_kursi):
            for row in range(len(layout)):
                for col in range(len(layout[row])):
                    if layout[row][col] == 0:  # Jika kursi terisi
                        layout[row][col] = 1  # Kembalikan status kursi
                        buttons[frame_index][row][col].config(bg="green", state="normal")  # Ubah warna dan aktifkan tombol
        pilihan_kursi.clear()
        
    def konfirmasi_kursi():
        if pilihan_kursi:
            print("Kursi yang dipilih:", ", ".join(pilihan_kursi))
            with open("kursi_pesanan.csv","a") as file:
                for kursi in pilihan_kursi:
                    file.write(f"{film_judul},{kursi}\n")
        # Ambil harga tiket dari data film
            harga_tiket = 0
            try:
                film_data = pd.read_csv("film_data.csv")
                harga_tiket = film_data.loc[film_data["judul"] == film_judul, "harga"].values[0]
            except Exception as e:
                print(f"Error fetching ticket price: {e}")

            # Panggil hal_konfirmasi dengan informasi yang dibutuhkan
            from hal_konfirmasi import hal_konfirmasi
            hal_kursi.destroy()
            hal_konfirmasi(film_judul, pilihan_kursi, harga_tiket, username)
        else:
            print("Tidak ada kursi yang dipilih.")

    reset_button = tk.Button(hal_kursi,width=20, text="Reset Kursi",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=reset_kursi)
    reset_button.grid(row=3, column=2)
    konfirmasi_button = tk.Button(hal_kursi,width=20, text="Konfirmasi",fg="#000000", bg="#C8102E",font=('Georgian', 16), command=konfirmasi_kursi)
    konfirmasi_button.grid(row=3, column=1)
    
    def open_hal_film():
        from hal_film import hal_film
        hal_kursi.destroy()
        hal_film(username)
        
    back_button = tk.Button(hal_kursi, width=8, height=1 ,text="balek",fg="#000000", bg="#C8102E",font=('Georgian', 12),command=open_hal_film)
    back_button.place(x=20, y=700 - 20 )

    hal_kursi.mainloop()
