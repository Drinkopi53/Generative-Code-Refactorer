# Generative Code Refactorer

Proyek ini adalah implementasi dari **Generative Code Refactorer** seperti yang dijelaskan dalam Dokumen Persyaratan Produk (PRD). Ini adalah alat berbasis web yang memanfaatkan kecerdasan buatan (disimulasikan dalam MVP ini) untuk menganalisis dan merefaktor kode Python, mengubahnya menjadi versi yang lebih modern, efisien, dan mudah dibaca.

## Ikhtisar Proyek

Tujuan dari aplikasi ini adalah untuk membantu pengembang Python dalam meningkatkan kualitas kode mereka secara otomatis. Pengguna dapat memasukkan skrip Python mereka, dan aplikasi akan memberikan versi yang telah direfaktor bersama dengan perbandingan berdampingan (diff) yang jelas yang menyoroti perubahan yang dibuat.

## Fitur MVP

*   **Antarmuka Berbasis Web**: UI yang sederhana dan bersih untuk memasukkan kode Python.
*   **Refaktorisasi Kode (Simulasi)**: Menerapkan aturan refaktorisasi dasar untuk menunjukkan konsep.
*   **Tampilan Perbandingan (Diff)**: Menampilkan perbandingan berdampingan yang jelas antara kode asli dan kode yang direfaktor.

## Teknologi yang Digunakan

*   **Backend**: Python dengan kerangka kerja Flask.
*   **Frontend**: HTML5 standar dengan CSS.
*   **Pustaka Python**: `difflib` untuk menghasilkan perbandingan kode.

## Cara Menjalankan Aplikasi

Untuk menjalankan aplikasi ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

1.  **Clone Repositori**:
    ```bash
    git clone <URL_REPOSITORI>
    cd generative-code-refactorer
    ```

2.  **Buat dan Aktifkan Lingkungan Virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Di Windows, gunakan `venv\Scripts\activate`
    ```

3.  **Instal Dependensi**:
    Pastikan Anda memiliki `pip` yang terinstal, lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi**:
    ```bash
    python app/main.py
    ```

5.  **Akses Aplikasi**:
    Buka browser web Anda dan navigasikan ke `http://127.0.0.1:5000`. Anda akan melihat antarmuka pengguna tempat Anda dapat memasukkan kode Python Anda untuk direfaktor.