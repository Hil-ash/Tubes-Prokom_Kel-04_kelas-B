# Kelompok-4

## Deskripsi Proyek
Proyek ini merupakan bagian dari tugas kelompok dalam mata kuliah prokom. Kami mengembangkan sebuah program Python untuk memesan tiket bioskop.

## Daftar Anggota Kelompok
- **[Fahrul Rafi Widodo]** (NIM: I0324078)
- **[Hilmy Ashshiddiqi]** (NIM: I0324081)
- **[Muhamad Khoirun Nur]** (NIM: I0324085)

## Fitur Utama
1. **[Halaman Utama]** - [Menampilkan pilihan sign in, sign up, dan exit].
2. **[Fitur Login dan Registrasi]** - [Sign in untuk masuk sebagai pengguna atau admin dan sign up untuk pendaftaran pengguna baru].
3. **[Fitur Menu Pengguna]** - [Pesan tiket untuk pilih film, kursi dan konfirmasi pesanan sadangkan cancel tiket untuk Melihat daftar tiket yang sudah dipesan dan membatalkannya].
4. **[Fitur Admin]** - [Dapat menghapus film, menambah film, reset kursi, dan melihat riwayat pemesanan].
5. **[Konfirmasi dan Cetak Tiket]** - [Menampilkan struk pemesanan tiket dan menyimpan tiket dalam file .txt].
6. **[Manajemen Data]** - [Menggunakan file csv untuk menyimpan data akun pengguna, data akun admin, data film (judul, harga, gambar), data kursi yang dipesan, dan riwayat pemesanan].

## Struktur Proyek
```
Kelompok-4/
|-- main.py
|-- hal_utama.py
|-- hal_sigh_up.py
|-- hal_sigh_in.py
|-- hal_menu.py
|-- hal_film.py
|-- hal_kursi.py
|-- hal_konfirmasi.py
|-- hal_cancel.py
|-- hal_penutup.py
|-- hal_admin.py
|-- hal_tambah_film.py
|-- hal_hapus_film.py
|-- hal_reset_kursi.py
|-- hal_histori_pesanan.py
|-- user_data.csv
|-- admin_data.csv
|-- film_data.csv
|-- kursi_pesanan.csv
|-- pesanan_data.csv
|-- tiket.txt
|-- README.md
```

## Cara Menjalankan Proyek
1. Pastikan Python 3.13.0 dan library pandas dan pillow sudah terinstall di komputer Anda.
2. Clone repositori ini:
   ```bash
   git clone https://github.com/Hil-ash/Kelompok-4.git
   ```
3. Masuk ke direktori proyek:
   ```bash
   cd Kelompok-4
   ```
4. Jalankan file utama:
   ```bash
   python main.py
   ```

## Teknologi yang Digunakan
- Python 3.13.0
- Pandas (untuk manipulasi data)
- Pillow (untuk memproses gambar)


