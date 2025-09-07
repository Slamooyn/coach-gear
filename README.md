# TUGAS PBP COACH-GEAR
Nama: Muhammad Salman Fahri<br>
NPM: 2406343514<br>
Kelas: PBP F<br>
Link Deployment PWS: [CoachGear](https://muhammad-salman42-coachgear.pbp.cs.ui.ac.id/)


<details align="justify">
    <summary><b>Tugas 2</b></summary>

1.Pertama-tama saya membuat repository baru di GitHub dengan nama `coach-gear`, kemudian saya clone repository tersebut ke lokal. Setelah itu saya membuka direktori hasil clone di VSCode, membuat serta mengaktifkan virtual environment untuk mengisolasi proyek dari proyek lain, lalu melakukan instalasi dependencies yang dibutuhkan. Selanjutnya saya membuat proyek Django bernama `coach_gear_site`, menambahkan konfigurasi untuk development lokal dan production deployment melalui file `.env` dan `.env.prod`, serta memodifikasi `settings.py` untuk pengaturan perizinan akses.  

Setelah itu saya membuat aplikasi `main` di direktori `coach-gear` dengan menjalankan perintah `python manage.py startapp main` dan mendaftarkannya pada proyek `coach_gear_site`. Pada aplikasi `main`, saya membuat direktori `templates` dan menambahkan file `main.html` untuk kebutuhan Tugas 2. Kemudian saya menambahkan konfigurasi routing di `coach_gear_site/urls.py` untuk aplikasi `main`, serta membuat fungsi `show_main` di `main/views.py` yang menampilkan template `main.html` berisi nama aplikasi, nama, dan kelas. Untuk melengkapinya, saya juga membuat file `main/urls.py` guna memetakan fungsi `show_main` ke aplikasinya.  

Selanjutnya saya membuat model `Product` dengan atribut berupa `name` (CharField), `price` (IntegerField), `description` (TextField), `thumbnail` (URLField), `category` (CharField), dan `is_featured` (BooleanField). Setelah model selesai dibuat, saya membuat project baru di PWS dan menyesuaikan environment dengan `.env.prod`. Pada `settings.py`, saya menambahkan URL deployment `muhammad-salman42-coachgear.pbp.cs.ui.id`. Setelah konfigurasi selesai, saya menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mempersiapkan database. Terakhir, saya menyambungkan repository dengan PWS, menjalankan project command, melakukan build, dan melakukan push dengan perintah `git push pws master` untuk deployment.

</details>


