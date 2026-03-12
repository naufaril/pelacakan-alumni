# Sistem Pelacakan Alumni

Sistem Pelacakan Alumni merupakan aplikasi berbasis web yang digunakan untuk membantu admin kampus dalam melakukan pelacakan alumni melalui berbagai platform online seperti LinkedIn dan Google Scholar. Sistem ini juga dapat digunakan untuk menghasilkan data awal dalam proses **Tracer Study Alumni**.

Aplikasi ini dibuat menggunakan teknologi **Python (Flask) untuk backend** dan **HTML, CSS, JavaScript untuk frontend**.

---

## Fitur Sistem

Fitur utama pada aplikasi ini antara lain:

1. **Manajemen Data Alumni**
   - Menambahkan data alumni
   - Menampilkan daftar alumni

2. **Pelacakan Alumni**
   - Melakukan pencarian data alumni berdasarkan nama
   - Simulasi pencarian melalui platform:
     - LinkedIn
     - Google Scholar

3. **Validasi Data**
   - Sistem memberikan status hasil pencarian alumni.

4. **Dashboard Hasil Pelacakan**
   - Menampilkan informasi pekerjaan alumni
   - Menampilkan institusi penelitian alumni

---

## Teknologi yang Digunakan

| Komponen | Teknologi |
|--------|-----------|
| Backend | Python Flask |
| Frontend | HTML, CSS, JavaScript |
| Penyimpanan Data | JSON |
| Version Control | GitHub |

---

## Struktur Project
pelacakan-alumni
│
├── app.py
├── alumni.json
│
├── templates
│ └── index.html
│
├── static
│ ├── style.css
│ └── script.js
│
└── README.md

---

## Cara Menjalankan Aplikasi

### 1. Clone Repository


git clone https://github.com/username/pelacakan-alumni.git


Masuk ke folder project


cd pelacakan-alumni


---

### 2. Install Dependency

Pastikan Python sudah terinstall.


pip install flask


atau


pip3 install flask


---

### 3. Jalankan Server


python app.py


atau


python3 app.py


---

### 4. Buka Browser


http://localhost:5000


---

## Contoh Tampilan Sistem

Halaman utama menampilkan:

- Form tambah alumni
- Tabel data alumni
- Tombol pelacakan alumni
- Hasil pelacakan alumni

---

## Pengujian Sistem

Pengujian sistem dilakukan untuk memastikan aplikasi berjalan dengan baik berdasarkan beberapa aspek kualitas perangkat lunak.

| No | Fitur | Skenario Pengujian | Hasil | Status |
|----|------|--------------------|------|------|
| 1 | Menampilkan Data Alumni | Membuka halaman utama | Data tampil pada tabel | ✅ Berhasil |
| 2 | Tambah Alumni | Mengisi form tambah alumni | Data tersimpan | ✅ Berhasil |
| 3 | Pelacakan Alumni | Menekan tombol lacak | Data pelacakan muncul | ✅ Berhasil |
| 4 | API Backend | Request ke endpoint `/search` | Response JSON berhasil | ✅ Berhasil |

---

## Link publish web
Website dapat diakses melalui
https://pelacakan-alumni--naufaril.replit.app
