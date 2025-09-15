# TUGAS PBP COACH-GEAR
Nama: Muhammad Salman Fahri<br>
NPM: 2406343514<br>
Kelas: PBP F<br>
Link Deployment PWS: [CoachGear](https://muhammad-salman42-coachgear.pbp.cs.ui.ac.id/)


<details align="justify">
    <summary><b>Tugas 2</b></summary>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama saya membuat repository baru di GitHub dengan nama `coach-gear`, kemudian saya clone repository tersebut ke lokal. Setelah itu saya membuka direktori hasil clone di VSCode, membuat serta mengaktifkan virtual environment untuk mengisolasi proyek dari proyek lain, lalu melakukan instalasi dependencies yang dibutuhkan. Selanjutnya saya membuat proyek Django bernama `coach_gear_site`, menambahkan konfigurasi untuk development lokal dan production deployment melalui file `.env` dan `.env.prod`, serta memodifikasi `settings.py` untuk pengaturan perizinan akses.  

Setelah itu saya membuat aplikasi `main` di direktori `coach-gear` dengan menjalankan perintah `python manage.py startapp main` dan mendaftarkannya pada proyek `coach_gear_site`. Pada aplikasi `main`, saya membuat direktori `templates` dan menambahkan file `main.html` untuk kebutuhan Tugas 2. Kemudian saya menambahkan konfigurasi routing di `coach_gear_site/urls.py` untuk aplikasi `main`, serta membuat fungsi `show_main` di `main/views.py` yang menampilkan template `main.html` berisi nama aplikasi, nama, dan kelas. Untuk melengkapinya, saya juga membuat file `main/urls.py` guna memetakan fungsi `show_main` ke aplikasinya.  

Selanjutnya saya membuat model `Product` dengan atribut berupa `name` (CharField), `price` (IntegerField), `description` (TextField), `thumbnail` (URLField), `category` (CharField), dan `is_featured` (BooleanField). Setelah model selesai dibuat, saya membuat project baru di PWS dan menyesuaikan environment dengan `.env.prod`. Pada `settings.py`, saya menambahkan URL deployment `muhammad-salman42-coachgear.pbp.cs.ui.id`. Setelah konfigurasi selesai, saya menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mempersiapkan database. Terakhir, saya menyambungkan repository dengan PWS, menjalankan project command, melakukan build, dan melakukan push dengan perintah `git push pws master` untuk deployment.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 'urls.py', 'views.py', 'models.py', dan berkas html.
![Diagram Django](/public/Diagram.jpeg)

Ketika client mengirimkan sebuah HTTP request ke server Django, permintaan tersebut akan diproses dengan mencocokkan URL yang diminta terhadap pola yang sudah didefinisikan di dalam file `urls.py`. File ini berfungsi sebagai pengatur route yang menghubungkan URL dengan fungsi di aplikasi 'main'. Setelah URL sesuai ditemukan, request diteruskan ke `views.py`, yang bertugas mengelola logika seperti sebuah fungsi. Pada tahap ini, `views.py` dapat mengambil atau memanipulasi data melalui `models.py`, yang merupakan komponen untuk mengatur serta mengelola data aplikasi melalui database. Setelah memperoleh data yang dibutuhkan, `views.py` akan merender template HTML dengan data tersebut, sehingga menghasilkan tampilan akhir yang siap dikirimkan ke client. Hasil akhirnya berupa response HTML yang telah diproses oleh Django dan ditampilkan di browser client.

## Jelaskan peran 'settings.py' dalam proyek Django!
`settings.py` adalah file konfigurasi utama dalam sebuah proyek Django. Semua pengaturan inti proyek ditempatkan di sini, seperti konfigurasi database, daftar aplikasi yang terdaftar di `INSTALLED_APPS`, `ALLOWED_HOST`, serta konfigurasi tambahan untuk deployment. Singkatnya, file ini adalah pusat pengaturan yang mengatur bagaimana proyek Django berjalan, baik di lingkungan development maupun production.

## Bagaimana cara kerja migrasi database di Django?
migrasi di Django adalah proses untuk menjaga agar struktur database selalu sesuai dengan definisi model yang ada di aplikasi. Jadi, setiap kali kita menambahkan, mengubah, atau menghapus atribut di dalam `models.py`, Django tidak langsung mengubah database, tapi menyimpannya dulu sebagai perubahan skema.Dengan perubahan itu kemudian diterjemahkan menjadi file migration, kaya semacam catatan yang isinya instruksi tentang apa yang harus dilakukan pada database. Setelah file migrasi dibuat dengan perintah `python manage.py makemigrations`, langkah berikutnya adalah menerapkan perubahan tersebut ke database dengan perintah `python manage.py migrate`. 

Jadi cara kerja migrasi di Django bisa dipahami sebagai jembatan antara kode Python pada `models.py` dengan struktur di dalam database. Ketika perintah `python manage.py makemigrations` dijalankan, Django akan membandingkan kondisi model saat ini dengan migrasi sebelumnya, lalu membuat file migrasi baru yang berisi perubahan dari sebuah model. File migrasi ini sifatnya belum memengaruhi database, melainkan hanya mendokumentasikan rencana perubahan. Setelah itu, saat kita menjalankan `python manage.py migrate`, Django mengeksekusi isi file migrasi tersebut dengan menghasilkan query SQL yang sesuai dengan database yang digunakan, lalu menerapkannya langsung ke dalam database. Dengan cara ini, setiap perubahan data model tercatat, dapat dikelola bertahap, dan bisa di-rollback atau dijalankan ulang bila diperlukan.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, salah satu alasan Django dipakai sebagai permulaan pembelajaran adalah karena framework ini sudah digunakan oleh banyak perusahaan sejak lama dan terbukti stabil. Django juga berbasis Python, bahasa pemrograman yang sudah saya pelajari sejak semester satu, sehingga lebih mudah dipahami. Selain itu, Django adalah framework full-stack yang bisa digunakan untuk mengembangkan sisi backend sekaligus menyediakan frontend melalui sistem templating HTML. Hal ini membuat Django cocok sebagai langkah awal untuk memahami pengembangan perangkat lunak secara menyeluruh, mulai dari pengolahan data hingga penyajian tampilan kepada pengguna.

Django memang bisa dipakai untuk frontend lewat templating, tapi dia bukan framework frontend murni seperti React atau Vue. Jadi lebih tepatnya Django itu framework backend dengan kemampuan templating untuk menampilkan HTML.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Saya tidak memiliki feedback khusus, karena tutorial 1 sudah cukup jelas dan membantu dalam memahami materi.
</details>
<details align="justify">
    <summary><b>Tugas 3</b></summary>

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan aspek penting dalam pengimplementasian suatu platform karena bertujuan untuk memastikan bahwa pertukaran data antar komponen sistem (seperti antara frontend dan backend atau antar microservices) dilakukan dengan cara yang efisien, aman, dan konsisten. Data Delivery menjadi penting karena kebutuhan pertukaran informasi yang tepat secara real-time dan memfasilitasi komunikasi yang seamless antar komponen yang berbeda dalam sistem.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih unggul karena formatnya mudah dibaca baik oleh manusia. Selain itu, JSON memiliki ukuran yang lebih ringkas dibandingkan XML dan lebih sederhana untuk diproses dengan bahasa pemrograman yang umum digunakan dalam pengembangan web seperti JavaScript. Hal ini membuat JSON lebih populer karena menawarkan efisiensi yang lebih baik dalam pengiriman data di web.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` dipakai pada objek form untuk melakukan validasi data sekaligus menangani error. Fungsi dari metode ini adalah menyaring data yang masuk dan memastikan hanya data yang sudah lolos pengecekan serta dalam kondisi bersih yang akan diteruskan ke database.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita butuh `csrf_token` di form Django supaya sistem bisa yakin kalau request yang dikirim bener-bener datang dari user itu sendiri, bukan dari orang lain. Jadi, `csrf_token` ini semacam "tanda tangan unik" yang ikut dikirim tiap kali user submit form. Tujuannya buat ngelindungin aplikasi dari serangan CSRF (Cross-Site Request Forgery), yaitu serangan yang numpang sesi login user buat ngejalanin aksi yang sebenarnya nggak pernah diminta user.

Kalau kita nggak pakai `csrf_token`, penyerang bisa bikin halaman atau script jahat yang ngirim request ke aplikasi kita pakai akun user yang lagi login. Akibatnya bisa macem-macem, mulai dari ganti data, transaksi tanpa izin, sampai nyolong informasi pribadi. Karena nggak ada token buat ngecek, sistem bakal nganggep request itu sah-sah aja.

Intinya, `csrf_token` ini kayak pagar pengaman. Tanpa itu, aplikasi jadi gampang dimanipulasi lewat request palsu yang seolah-olah asli.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama saya membuat fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`, lalu melakukan mapping route untuk masing-masing fungsi tersebut di `urls.py` di direktori main. Setelah itu, saya menambahkan fungsi `product_add` dan `product_details` di views.py. Fungsi product_add digunakan untuk menambahkan produk baru, sedangkan `product_details` digunakan untuk menampilkan halaman detail dari setiap objek produk yang dibuat.

Selanjutnya, saya membuat `forms.py` di direktori main. File ini berfungsi untuk membuat, mengelola, dan memvalidasi form agar lebih mudah digunakan di `views.py` maupun di template.

Saya juga membuat direktori templates pada root utama dan menambahkan file `base.html`. File base.html berfungsi sebagai template induk yang menyimpan struktur utama aplikasi, sehingga halaman lain bisa extends dari situ tanpa perlu menulis ulang kode yang sama.

Kemudian, saya membuat file `product_add.html` dan `product_details.html` untuk menampilkan halaman penambahan produk serta halaman detail produk. Kedua file ini sudah terintegrasi dengan fungsi yang ada di `views.py` serta model yang telah dibuat.

Terakhir, saya mengubah `main.html` agar menyesuaikan dengan kebutuhan Tugas 3, sehingga tampilannya selaras dengan fungsionalitas baru yang sudah ditambahkan.

## Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Sejauh ini tidak ada, penjelasannya sudah sangat jelas dan sangat membantu
## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

1.`show_xml`
![Foto postman xml](/public/FotoShowXml.jpeg)

2.`show_xml_by_id`
![Foto postman xml_id](/public/FotoShowXmlById.jpeg)

3.`show_json`
![Foto postman json](/public/FotoShowJson.jpeg)

4.`show_json_by_id`
![Foto postman json_id](/public/FotoShowJsonById.jpeg)

</details>


