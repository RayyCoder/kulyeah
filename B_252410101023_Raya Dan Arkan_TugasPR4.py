import pandas as pd
import os 
dataMahasiswa = {
    'Nama' : ['RAYA DAN ARKAN', 'MUHAMMAD FATH RIFKY HALMAR', 'NAYSILA AMELIA PUTRI', 'ANGGUN CANTIKA BELLIANA HASTINE', 'MAULANA FATHIR HIDAYAT', 'MUHAMMAD RADITYA ZIDANE', 'MIRZA UCHMAL GANI', 'CAESYA VALENZIA AGATHA', 'IBNU ATHA ADHANY', 'KIRANA CINTA LESTARI'],
    'NIM'  : [252410101023, 252410101043, 252410101022, 252410101036, 252410101046, 252410102055, 252410102107, 252410102008, 252410103103, 252410103022],
    'Program Studi' : ['Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi', 'Teknologi Informasi', 'Teknologi Informasi', 'Teknologi Informasi', 'Informatika', 'Informatika']
}
dataMahasiswa = pd.DataFrame(dataMahasiswa)
dataMahasiswa.to_csv('dataMahasiswa.csv', index=False)


def menampilkan():
    os.system('cls')
    print('===== DATA MAHASISWA TERBARU =====')
    df = pd.read_csv('dataMahasiswa.csv')
    print(df)
    input('Tekan Enter Untuk Kembali')
    utama()

def penambahan():
    os.system('cls')
    print('===== SILAHKAN MENAMBAH DATA BARU =====')
    nama = input('Masukkan Nama Mahasiswa: ')
    nim = int(input('Masukkan NIM: '))
    prodi = input('Masukkan Program Studi: ')
    df = pd.read_csv('dataMahasiswa.csv')
    df = pd.concat([df, pd.DataFrame([{'Nama': nama, 'NIM': nim, 'Program Studi': prodi} ])], ignore_index= True)
    df.to_csv('dataMahasiswa.csv', index=False)
    print('Data Berhasil Ditambahkan')
    input('Tekan Enter Untuk Kembali Ke Menu Awal')
    utama()

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

utama()