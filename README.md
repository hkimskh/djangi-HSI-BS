# djangi-HSI-BS
...existing code...
# Website Profil Santri — HSI Boarding School

Sebuah proyek Django sederhana yang menampilkan profil santri, jadwal, galeri, dan form feedback.
Project ini menggunakan aplikasi `santri` dan template Django standar.

Fitur utama
- Halaman utama (portfolio) — [webprofile/templates/home.html](webprofile/templates/home.html)
- Aplikasi `santri` dengan halaman: beranda, biodata, jadwal, galeri, feedback
  - URL app: [webprofile/santri/urls.py](webprofile/santri/urls.py)
  - View contoh: [`santri.views.santri_home`](webprofile/santri/views.py)

Struktur penting
- Manajemen & server: [webprofile/manage.py](webprofile/manage.py)
- Konfigurasi proyek: [`webprofile.settings`](webprofile/webprofile/settings.py)
- Template dasar: [webprofile/templates/base.html](webprofile/templates/base.html)
- Static CSS: [webprofile/static/style.css](webprofile/static/style.css)

Persiapan & menjalankan (lokal)
1. Buat virtual environment dan aktifkan:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install Django (versi yang sesuai, contoh):
   ```sh
   pip install "django>=6.0,<7.0"
   ```
3. Migrasi database:
   ```sh
   python webprofile/manage.py migrate
   ```
4. Jalankan server pengembangan:
   ```sh
   python webprofile/manage.py runserver
   ```
   Buka http://127.0.0.1:8000/ untuk melihat halaman utama.

Catatan pengembangan
- Static files didefinisikan di [`webprofile.settings`](webprofile/webprofile/settings.py) dan berada di folder [webprofile/static](webprofile/static).
- Template global berada di [webprofile/templates](webprofile/templates) dan template app `santri` di [webprofile/santri/templates/santri](webprofile/santri/templates/santri).
- Untuk menambahkan halaman baru, tambahkan view di [webprofile/santri/views.py](webprofile/santri/views.py) dan rute di [webprofile/santri/urls.py](webprofile/santri/urls.py).

Lisensi
- Tambahkan lisensi sesuai kebutuhan proyek.

...existing