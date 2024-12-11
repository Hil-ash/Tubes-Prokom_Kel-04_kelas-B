import tkinter as tk
import tkinter.messagebox as messagebox

def hal_Sigh_in():
    hal_Sigh_in = tk.Tk()
    hal_Sigh_in.title("Sistem Pemesanan Tiket Bioskop")
    hal_Sigh_in.geometry("1200x750")
    hal_Sigh_in.resizable(False,False)
    hal_Sigh_in.configure(bg='#000000')
    
    def open_hal_Utama():
        from hal_utama import hal_Utama
        hal_Sigh_in.destroy()
        hal_Utama()
    
    judul = tk.Label(hal_Sigh_in, text="Masukkan Akun" , font=('Georgia', 34), fg="#C8102E", bg="#000000")
    judul.pack(padx= 20 , pady= 100)
    
    frame = tk.Frame(hal_Sigh_in, bg="#000000", width=500, height=300, relief="ridge", borderwidth=0)
    frame.pack(padx= 50, pady=10)
    frame.pack_propagate(False)
    
    tk.Label(frame, text="Username", fg="#C8102E", bg="#000000", font=('Georgia', 16)).pack(padx=50, pady=10, fill=tk.X, expand=True)
    isi_username = tk.Entry(frame)
    isi_username.pack(padx=50, pady=10, fill=tk.X, expand=True)
    
    tk.Label(frame, text="Password", fg="#C8102E", bg="#000000", font=('Georgia', 16)).pack(padx=50, pady=10, fill=tk.X, expand=True)
    isi_password = tk.Entry(frame, show="*")
    isi_password.pack(padx=50, pady=10, fill=tk.X, expand=True)
    
    def Sign_in():
        A1 = isi_username.get()
        A2 = isi_password.get()
        username = A1

        if A1 == "" or A2 == "":
            messagebox.showinfo("Error", "Isi semuanya")
            return
        # Cek akun pengguna
        with open("user_data.csv", "r") as file:
            sukses = False
            for i in file:
                if i.strip():  # Mengabaikan baris kosong
                    try:
                        a, b = i.strip().split(",")
                        if a == A1 and b == A2:
                            sukses = True
                            break
                    except ValueError:
                        continue
        if sukses:
            messagebox.showinfo("Informasi", "Login Berhasil")
            from hal_menu import hal_menu
            hal_Sigh_in.destroy()
            hal_menu(username)
        else:
            # Cek akun admin
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
                messagebox.showinfo("Informasi", "Login Berhasil sebagai admin")
                hal_Sigh_in.destroy()
                from hal_admin import hal_admin
                hal_admin(username)
            else:
                messagebox.showinfo("Informasi", "Anda Belum Terdaftar")

    hal_Sigh_in.bind('<Return>', lambda event: Sign_in())

    button_masuk = tk.Button(frame, width=28 ,text="Mlebu" ,fg="#000000", bg="#C8102E", font=('Georgia', 16), command= Sign_in)
    button_masuk.pack(padx=50 , pady=40)
    
    back_button = tk.Button(hal_Sigh_in, width=8, height=1 ,text="Balek" ,fg="#000000", bg="#C8102E", font=('Georgia', 12), command= open_hal_Utama)
    back_button.place(x=20, y=700 - 20 )
    
    hal_Sigh_in.mainloop()
