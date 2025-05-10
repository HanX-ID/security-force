# Security Force 

Ini adalah script Python yang digunakan untuk memeriksa kekuatan password dan validitas email. Password akan diperiksa apakah tergolong umum berdasarkan **wordlist** yang disediakan (`password_umum.txt`). Selain itu, script ini juga menghitung skor kekuatan password berdasarkan kriteria seperti panjang password, keberadaan huruf besar/kecil, angka, dan simbol.

## Fitur
- Mengecek apakah password tergolong umum berdasarkan wordlist.
- Menilai kekuatan password (persentase 1-100%).
- Memeriksa validitas email dengan regex.
- Output hasil dalam bentuk persentase kekuatan password dan email.

## Tentang Wordlist
File `password_umum.txt` berisi **500.000 baris** password yang umum digunakan dan lemah secara keamanan. File ini digunakan untuk membandingkan apakah password yang Anda masukkan tergolong password yang mudah ditebak atau tidak.

## Persyaratan
- Python 3.x
- Library Python:
  - `termcolor` untuk pewarnaan output.
  
## Cara Menggunakan di Termux

### 1. Install Python dan Termcolor
Pastikan Termux sudah terinstal di perangkat Android Anda. Kemudian install Python dan `termcolor` dengan perintah berikut:

```bash
pkg update
pkg install python git
pip install termcolor
```
2. Clone Repository

Clone project dari GitHub:
```
git clone https://github.com/HanX-ID/security-force.git
cd security-force
```
3. Jalankan Script
```
python main.py
```
4. Input Data

Masukkan email dan password sesuai perintah:
```
Masukkan email: email@example.com
Masukkan password: example123
```
5. Hasil Output

Output akan menunjukkan validitas email dan kekuatan password:
```
[ Email    ] Valid
[ Password ] 75%
 - Password ini sangat umum
[ Total Kekuatan ] 80%
```
Author [HanX](https://github.com/HanX-ID)

