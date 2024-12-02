import tkinter as tk
import pandas as pd
import PIL
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def hal_Utama ():
    hal_Utama = tk.Tk()
    hal_Utama.title("Sistem Pemesanan Tiket Bioskop")
    hal_Utama.geometry("1200x750")
    hal_Utama.resizable(False,False)
    
    def open_sign_in():
        hal_Utama.destroy()
        hal_Sigh_in()
        
    def open_sign_up():
        hal_Utama.destroy()
        hal_Sigh_Up()
    
    judul = tk.Label(hal_Utama, text="Selamat Datang di CGV" , font=('Arial', 30))
    judul.pack(padx= 20 , pady= 70)
    
    frame = tk.Frame(hal_Utama, bg="lightblue", width=300, height=200, relief="ridge", borderwidth=2)
    frame.pack(padx= 50, pady=100)
    frame.pack_propagate(False)
    
    button = tk.Button(frame, width=20 ,text="Sigh In" ,font=(8), command= open_sign_in)
    button.pack(padx=50 , pady=40)
    button1 = tk.Button(frame, width=20 ,text="Sigh Up" ,font=(8), command= open_sign_up)
    button1.pack(padx=50 , pady=5)
    
    def exit():
        hal_Utama.destroy()
    
    Margin_kiri = 20
    Margin_bawah = 20
    button1 = tk.Button(hal_Utama, width=7, height=1 ,text="Keluar" ,font=(8),command=exit)
    button1.place(x=Margin_kiri, y=700 - Margin_bawah )
    

    
    hal_Utama.mainloop()

def hal_Sigh_in():
    hal_Sigh_in = tk.Tk()
    hal_Sigh_in.title("Sistem Pemesanan Tiket Bioskop")
    hal_Sigh_in.geometry("1200x750")
    hal_Sigh_in.resizable(False,False)
    
    def open_hal_Utama():
        hal_Sigh_in.destroy()
        hal_Utama()
    
    judul = tk.Label(hal_Sigh_in, text="Masukkan Akun" , font=('Arial', 25))
    judul.pack(padx= 20 , pady= 100)
    
    frame = tk.Frame(hal_Sigh_in, bg="lightblue", width=500, height=300, relief="ridge", borderwidth=2)
    frame.pack(padx= 50, pady=10)
    frame.pack_propagate(False)
    
    Username_1 = tk.Label(frame, bg="lightblue", text="Nama", font= 10)
    Username_1.pack(padx=50, pady=10, fill=X, expand=True)
    
    isi_username = tk.Entry(frame)
    isi_username.pack(padx=50, pady=10, fill=X, expand=True)
    
    Password_1 = tk.Label(frame, bg="lightblue", text="Password", font= 10)
    Password_1.pack(padx=50, pady=10, fill=X, expand=True)
    
    isi_password = tk.Entry(frame, show="*")
    isi_password.pack(padx=50, pady=10, fill=X, expand=True)
    
    def Sign_in ():
        A1 = isi_username.get()
        A2 = isi_password.get()
        
        if A1=="" or A2=="":
           messagebox.showinfo("Eror","isi semuanya")
        else :
            with open("user_data.csv", "r") as file:
                sukses = False
                for i in file:
                    # Mengabaikan baris kosong
                    if i.strip():  # Hanya memproses baris yang tidak kosong
                        try:
                            a, b = i.strip().split(",")  # Menggunakan strip untuk menghapus spasi
                            if a == A1 and b == A2:
                                sukses = True
                                break
                        except ValueError:
                            # Jika tidak bisa memisahkan menjadi dua nilai, abaikan baris ini
                            continue
            if sukses:
                global username
                username = A1
                messagebox.showinfo("Informasi", "Login Berhasil")
                hal_Sigh_in.destroy()
                hal_Film()
            else:
                    with open("admin_data.csv", "r") as file_admin:
                        admin_sukses = False
                        for j in file_admin:
                            if j.strip():  # Mengabaikan baris kosong
                                try:
                                    a_admin, b_admin = j.strip().split(",")
                                    if a_admin == A1 and b_admin == A2:
                                        admin_sukses = True
                                        break
                                except ValueError:
                                    continue
                    if admin_sukses:
                        # Jika akun admin ditemukan, lakukan aksi untuk akun admin
                        messagebox.showinfo("Informasi", "Login Berhasil sebagai admin")
                        hal_Sigh_in.destroy()
                        hal_admin()
                    else:
                        messagebox.showinfo("Informasi", "Anda Belum Terdaftar")

    
  
    button = tk.Button(frame, width=20 ,text="Masuk" ,font=(8), command= Sign_in)
    button.pack(padx=50 , pady=40)
    
    
    Margin_kiri = 20
    Margin_bawah = 20
    button1 = tk.Button(hal_Sigh_in, width=7, height=1 ,text="Kembali" ,font=(8), command= open_hal_Utama)
    button1.place(x=Margin_kiri, y=700 - Margin_bawah )
    
    
    
    hal_Sigh_in.mainloop()
    
username = ""  # Variabel global untuk menyimpan username
  
def hal_Sigh_Up():
   hal_Sigh_Up = tk.Tk()
   hal_Sigh_Up.title("Sistem Pemesanan Tiket Bioskop")
   hal_Sigh_Up.geometry("1200x750")
   hal_Sigh_Up.resizable(False,False)
   
   
   judul = tk.Label(hal_Sigh_Up, text="Silahkan buat Akun" , font=('Arial', 25))
   judul.pack(padx= 20 , pady= 100)
   
   frame = tk.Frame(hal_Sigh_Up, bg="lightblue", width=500, height=300, relief="ridge", borderwidth=2)
   frame.pack(padx= 50, pady=10)
   frame.pack_propagate(False)
   
   Username_1 = tk.Label(frame, bg="lightblue", text="Nama", font= 10)
   Username_1.pack(padx=50, pady=10, fill=X, expand=True)
   
   
   isi_username = tk.Entry(frame)
   isi_username.pack(padx=50, pady=10, fill=X, expand=True)
   
   Password_1 = tk.Label(frame, bg="lightblue", text="Password", font= 10)
   Password_1.pack(padx=50, pady=10, fill=X, expand=True)
   
   isi_password = tk.Entry(frame)
   isi_password.pack(padx=50, pady=10, fill=X, expand=True)
   
   def Sign_up ():
       A1 = isi_username.get()
       A2 = isi_password.get()
       
       if A1=="" or A2=="":
           messagebox.showinfo("Eror","isi semuanya")
       else :
           file = open("user_data.csv", "a")
           file.write("\n"+A1+","+A2)
           messagebox.showinfo("Informasi","Pembuatan berhasil")
           hal_Sigh_Up.destroy()
           hal_Utama()
   
   button = tk.Button(frame, width=20 ,text="Buat" ,font=(8), command= Sign_up)
   button.pack(padx=50 , pady=40)
   
   def open_hal_Utama():
        hal_Sigh_Up.destroy()
        hal_Utama()
    
   Margin_kiri = 20
   Margin_bawah = 20
   button2 = tk.Button(hal_Sigh_Up, width=7, height=1 ,text="Kembali" ,font=(8), command= open_hal_Utama)
   button2.place(x=Margin_kiri, y=700 - Margin_bawah )
   
   hal_Sigh_Up.mainloop()
   
def hal_Film():
    hal_Film = tk.Tk()
    hal_Film.title("Sistem Pemesanan Tiket Bioskop")
    hal_Film.geometry("1200x750")
    hal_Film.resizable(False,False)
    
    hal_Film.columnconfigure(0,weight=1)
    hal_Film.columnconfigure(1,weight=1)
    hal_Film.columnconfigure(2,weight=1)
    hal_Film.columnconfigure(3,weight=1)
    hal_Film.columnconfigure(4,weight=1)
    
    hal_Film.rowconfigure(0,weight=1)
    hal_Film.rowconfigure(1,weight=1)
    hal_Film.rowconfigure(2,weight=1)
    hal_Film.rowconfigure(3,weight=1)
    
    judul = tk.Label(hal_Film, text="Pilih Film", font=('Arial', 30))
    judul.grid(row=0,column=2 ,columnspan=2, sticky="we")

    # Membaca data film dari file CSV
    try:
        film_data = pd.read_csv("film_data.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "File film_data.csv tidak ditemukan.")
        return

    # Loop untuk membuat frame
    for i, row in film_data.iterrows():
        frame = tk.Frame(hal_Film, bg="lightblue", width=180, height=350, relief="ridge", borderwidth=2)
        frame.grid(row=1, column=i, padx=10, sticky="we")
        frame.pack_propagate(False)

        # Judul Film
        film_judul = tk.Label(frame, text=row["judul"], font=('Arial', 15), bg="lightblue", wraplength=160)
        film_judul.pack(pady=10)

        # Gambar Film
        try:
            img = Image.open(row["gambar"])  # Pastikan gambar ada di path ini
            img = img.resize((150, 200))  # Mengubah ukuran gambar
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=img_tk, bg="lightblue")
            #img_label.image = img_tk   Menyimpan referensi gambar
            img_label.pack(pady=10,padx=2)
        except Exception as e:
            print(f"Error loading image for {row['judul']}: {e}")

        # Harga Tiket
        harga = f"Rp {int(row['harga']):,}"  # Menggunakan int() untuk menghilangkan desimal dan format dengan ribuan pemisah
        harga_tiket = tk.Label(frame, text=harga, font=('Arial', 10), bg="lightblue")
        harga_tiket.pack(pady=5)
        
        def open_hal_kursi(film_judul):
            hal_Film.destroy()
            hal_kursi(film_judul)
        
        button1 = tk.Button(hal_Film, width=7, height=1 ,text="Pilih" ,font=(8), command=lambda film_judul=row["judul"]: open_hal_kursi(film_judul))
        button1.grid(row= 2, column=i)
        
    def open_hal_sign_in():
        hal_Film.destroy()
        hal_Sigh_in()
        
    Margin_kiri = 20
    Margin_bawah = 20
    button1 = tk.Button(hal_Film, width=7, height=1 ,text="Kembali" ,font=(8),command=open_hal_sign_in)
    button1.place(x=Margin_kiri, y=700 - Margin_bawah )
    
    hal_Film.mainloop()
    
def hal_kursi(film_judul):
    hal_kursi = tk.Tk()
    hal_kursi.title("Sistem Pemesanan Tiket Bioskop")
    hal_kursi.geometry("1200x750")  # Ukuran jendela disesuaikan untuk menampung 6 frame
    hal_kursi.resizable(False, False)
    
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

    
    hal_kursi.columnconfigure(0,weight=1)
    hal_kursi.columnconfigure(1,weight=1)
    hal_kursi.columnconfigure(2,weight=1)
    
    hal_kursi.rowconfigure(0,weight=1)
    hal_kursi.rowconfigure(1,weight=1)
    hal_kursi.rowconfigure(2,weight=1)
    hal_kursi.rowconfigure(3,weight=1)
    hal_kursi.rowconfigure(4,weight=1)
    
    judul = tk.Label(hal_kursi, text=f"Pilih kursi untuk {film_judul}" , font=('Arial', 25))
    judul.grid(row=0, column=0, columnspan=3)
    
    frame = tk.Frame(hal_kursi, bg="lightblue", width=500, height=300, relief="ridge", borderwidth=2)
    frame.grid(row=1,column=0, columnspan=3, sticky="we", padx=20)
    frame.pack_propagate(False)
    
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(1,weight=1)
    frame.columnconfigure(2,weight=1)
    
    frame.rowconfigure(0,weight=1)
    frame.rowconfigure(1,weight=1)
    frame.rowconfigure(2,weight=1)
    
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
    
    
    layout_kursi_1 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]

    layout_kursi_2 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]

    layout_kursi_3 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]

    buttons = []  # Menyimpan referensi tombol
    pilihan_kursi = []  # Menyimpan kursi yang dipilih

    def pilih_kursi(frame_index, row, col):
        if frame_index == 0 and layout_kursi_1[row][col] == 1:  # Jika kursi tersedia di frame 1
            layout_kursi_1[row][col] = 0  # Tandai kursi sebagai terisi
            buttons[0][row][col].config(bg="red", state="disabled")
            kursi_nomor = row * jumlah_kolom + col + 1# Ubah warna dan nonaktifkan tombol
            pilihan_kursi.append(chr(65 + frame_index) + str(kursi_nomor))  # Simpan pilihan kursi
        elif frame_index == 1 and layout_kursi_2[row][col] == 1:  # Jika kursi tersedia di frame 2
            layout_kursi_2[row][col] = 0
            buttons[1][row][col].config(bg="red", state="disabled")
            kursi_nomor = row * jumlah_kolom + col + 1
            pilihan_kursi.append(chr(65 + frame_index) + str(kursi_nomor))
        elif frame_index == 2 and layout_kursi_3[row][col] == 1:  # Jika kursi tersedia di frame 3
            layout_kursi_3[row][col] = 0
            buttons[2][row][col].config(bg="red", state="disabled")
            kursi_nomor = row * jumlah_kolom + col + 1
            pilihan_kursi.append(chr(65 + frame_index) + str(kursi_nomor))
            
    
    jumlah_kolom = 5
    buttons = []
    pilihan_kursi = []
    

    # Membuat grid kursi untuk frame 2 dan frame 3 dengan logika yang sama
    for frame_index, layout in enumerate([layout_kursi_1, layout_kursi_2, layout_kursi_3]):
        row_buttons = []
        for row in range(len(layout)):
            row_buttons.append([])
            for col in range(len(layout[row])):
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
        for frame_index, layout in enumerate([layout_kursi_1, layout_kursi_2, layout_kursi_3]):
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
            hal_kursi.destroy()
            hal_konfirmasi(film_judul, pilihan_kursi, harga_tiket, username)
        
        else:
            print("Tidak ada kursi yang dipilih.")
        
    reset_button = tk.Button(hal_kursi, text="Reset Kursi", command=reset_kursi)
    reset_button.grid(row=3, column=2)

    konfirmasi_button = tk.Button(hal_kursi, text="Konfirmasi", command=konfirmasi_kursi)
    konfirmasi_button.grid(row=3, column=1)
    
    def open_hal_film():
        hal_kursi.destroy()
        hal_Film()
    
    Margin_kiri = 20
    Margin_bawah = 20
    button1 = tk.Button(hal_kursi, width=7, height=1 ,text="Kembali" ,font=(8),command=open_hal_film)
    button1.place(x=Margin_kiri, y=700 - Margin_bawah )
 
    hal_kursi.mainloop()

print(f"Username yang digunakan: {username}")  
  
def hal_konfirmasi(film_judul, pilihan_kursi, harga_tiket, username):
    hal_konfirmasi = tk.Tk()
    hal_konfirmasi.title("Sistem Pemesanan Tiket Bioskop")
    hal_konfirmasi.geometry("1200x750")
    hal_konfirmasi.resizable(False,False)
    
    judul = tk.Label(hal_konfirmasi, text="Konfirmasi Pesanan" , font=('Arial', 25))
    judul.pack(padx= 20 , pady= 20)
    
    #frame = tk.Frame(hal_konfirmasi, bg="lightblue", width=500, height=400, relief="ridge", borderwidth=2)
    #frame.pack(padx= 50, pady=10)
    
    # Menghitung panjang maksimum dari string yang relevan
    max_length = max(len(username), len(film_judul), len(', '.join(pilihan_kursi)), len(f"Rp {harga_tiket:,}"))
    print(max_length)
    pembatas = "=" * (max_length+20)
    judul = "         Tiket Bioskop          "
    # Menampilkan informasi pemesanan
    jumlah_kursi = len(pilihan_kursi)
    total_harga = jumlah_kursi*harga_tiket

    struk_text = f"{pembatas}\n{judul}\n{pembatas}\n"
    struk_text += f"{'Nama Pengguna':<20}: {username}\n"
    struk_text += f"{'Nama Film':<20}: {film_judul}\n"
    struk_text += f"{'Jumlah Kursi':<20}: {jumlah_kursi}\n"
    struk_text += f"{'Kode Kursi':<20}: {', '.join(pilihan_kursi)}\n"
    struk_text += f"{'Total Harga':<20}: Rp {total_harga:,}\n"
    struk_text += f"{pembatas}\n"

    struk_label = tk.Label(hal_konfirmasi, text=struk_text, font=('Arial',20), bg="lightblue", justify="left")
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
        hal_Film()
        
    def open_hal_penutup ():
        with open("tiket.txt", "a+") as file:
            file.write(struk_text)
        hal_konfirmasi.destroy()
        hal_penutup()
            
    
    konfirmasi_button = tk.Button(hal_konfirmasi, text="Konfirmasi Pesanan", command=open_hal_penutup)
    konfirmasi_button.pack(padx=50, pady=10)
    
    cancel_button = tk.Button(hal_konfirmasi, text="Batalkan Pesanan", command=batalkan_pesanan)
    cancel_button.pack(padx= 50, pady= 10)

    hal_konfirmasi.mainloop()
    
def hal_penutup():
    hal_penutup = tk.Tk()
    hal_penutup.title("Sistem Pemesanan Tiket Bioskop")
    hal_penutup.geometry("1200x750")
    hal_penutup.resizable(False,False)
    
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
    judul = tk.Label(frame, text=penutup , font=('Arial', 25), justify="center", bg="lightblue")
    judul.pack(pady= 10, padx= 10)
    
    def pesan_lagi():
        hal_penutup.destroy()
        hal_Film()
    
    def keluar():
        hal_penutup.destroy()
    
    konfirmasi_button = tk.Button(hal_penutup, text="Pesan lagi", command=pesan_lagi)
    konfirmasi_button.pack(padx=50, pady=10)
    
    cancel_button = tk.Button(hal_penutup, text="Keluar", command=keluar)
    cancel_button.pack(padx= 50, pady= 10)
    
    hal_penutup.mainloop()
    
    
def hal_admin():
    hal_admin = tk.Tk()
    hal_admin.title("Sistem Pemesanan Tiket Bioskop")
    hal_admin.geometry("1200x750")
    hal_admin.resizable(False,False)
    
    
    hal_admin.mainloop()


hal_Utama()