import pandas as pd # Melakukan import library pandas
import os           # Melakukan import library os

# Membuat Data Awal (Nama, NIM, Program Studi)
dataMahasiswa = {
    'Nama' : ['RAYA DAN ARKAN', 'MUHAMMAD FATH RIFKY HALMAR', 'NAYSILA AMELIA PUTRI', 'ANGGUN CANTIKA BELLIANA HASTINE', 'MAULANA FATHIR HIDAYAT', 'MUHAMMAD RADITYA ZIDANE', 'MIRZA UCHMAL GANI', 'CAESYA VALENZIA AGATHA', 'IBNU ATHA ADHANY', 'KIRANA CINTA LESTARI'],
    'NIM'  : [252410101023, 252410101043, 252410101022, 252410101036, 252410101046, 252410102055, 252410102107, 252410102008, 252410103103, 252410103022],
    'Program Studi' : ['Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi', 'Teknologi Informasi', 'Teknologi Informasi', 'Teknologi Informasi', 'Informatika', 'Informatika']
}
dataMahasiswa = pd.DataFrame(dataMahasiswa) # Menjadikan data menjadi dataframe
dataMahasiswa.to_csv('dataMahasiswa.csv', index=False) # Memasukkan data ke csv

# Membuat Fungsi 'menampilkan()' untuk menampilkan keseluruhan data terbaru
def menampilkan():
    os.system('cls')
    print('===== DATA MAHASISWA TERBARU =====')
    df = pd.read_csv('dataMahasiswa.csv')
    print(df)
    input('Tekan Enter Untuk Kembali ke Menu Utama....')
    utama()

# Membuat Fungsi 'penambahan()' yang berisi program untuk menambahkan data yang belum ada di data awal 
def penambahan():
    os.system('cls')
    print('===== SILAHKAN MENAMBAH DATA BARU =====')
    nama = input('Masukkan Nama Mahasiswa: ')
    nim = int(input('Masukkan NIM: '))
    prodi = input('Masukkan Program Studi: ')
    df = pd.read_csv('dataMahasiswa.csv')
    df = pd.concat([df, pd.DataFrame([{'Nama': nama, 'NIM': nim, 'Program Studi': prodi} ])], ignore_index= True)
    df.to_csv('dataMahasiswa.csv', index=False)
    print('---- Data Berhasil Ditambahkan ----')
    print('Berikut Adalah Data yang Baru Saja Anda Tambahkan:')
    print(df.tail(1))
    input('Tekan Enter Untuk Kembali Ke Menu Utama....')
    utama()

# Membuat Fungsi 'ubah()' yang berisi program untuk user dapat merubah atau mengedit data yang sudah ada
def ubah():
    os.system('cls')
    print('===== MENU PERUBAHAN DATA =====')
    df = pd.read_csv('dataMahasiswa.csv')
    print(df)
    nama_mhs = input('Pilih dan Masukkan Nama Mahasiswa yang ingin diubah datanya: ')
    ubah_nim = int(input('Masukkan NIM baru: '))
    ubah_prodi = input('Masukkan Program Studi baru: ')
    df.loc[df['Nama'] == nama_mhs, ['NIM', 'Program Studi']] = [ubah_nim, ubah_prodi]
    df.to_csv('dataMahasiswa.csv', index=False)
    print(f"---- Data Mahasiswa Bernama '{nama_mhs}' Telah Berhasil Diubah ----")
    print('Berikut Detail Perubahannya:')
    print(df[df['Nama'] == nama_mhs])
    input('Tekan Enter Untuk Kembali ke Menu Utama....')
    utama()

# Membuat Fungsi 'hapus()' yang berisi program untuk user menghapus sebagian atau beberapa data yang ada
def hapus():
    os.system('cls')
    print('===== MENU PENGHAPUSAN DATA =====')
    df = pd.read_csv('dataMahasiswa.csv')
    print(df)
    nama = input("Masukkan Nama Mahasiswa yang ingin dihapus datanya: ")
    df = df[df['Nama'] != nama]
    df.to_csv('dataMahasiswa.csv', index=False)
    print(f"---- Data Mahasiswa Bernama '{nama}' Telah Berhasil Dihapus ----")
    input('Tekan Enter Untuk Kembali ke Menu Utama....')
    utama()

# Membuat Fungsi 'utama()' yang berisi kumpulan menu utama, juga sebagai home/beranda
def utama():
    os.system('cls')
    print('===== SISTEM PENGELOLA DATA MAHASISWA =====')
    print('Pilih Salah Satu Menu dibawah Ini')
    print('[1] Tampilkan Keseluruhan Data')
    print('[2] Tambah Data')
    print('[3] Ubah Data')
    print('[4] Hapus Data')
    pemilihan = int(input('Silahkan Ketik Nomor yang Tersedia untuk Mengakses Menu. [1][2][3][4]: '))
    if pemilihan == 1:
        menampilkan()
    if pemilihan == 2:
        penambahan()
    if pemilihan == 3:
        ubah()
    if pemilihan == 4:
        hapus()

utama()