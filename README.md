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
<details align="justify">
    <summary><b>Tugas 4</b></summary>

## Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.
`AuthenticationForm` di Django adalah sebuah form bawaan dari modul `django.contrib.auth.forms` yang digunakan untuk proses `login` atau autentikasi pengguna. Form ini secara default hanya memiliki dua field utama, yaitu `username` dan `password`. Saat divalidasi, Django akan secara otomatis melakukan pengecekan apakah kombinasi `username` dan `password` yang dimasukkan sesuai dengan data yang ada, sekaligus memastikan bahwa akun pengguna tersebut aktif. Jika data valid, objek user dapat diakses melalui `method form.get_user()`.

Kelebihan dari `AuthenticationForm` terletak pada kemudahannya karena sudah terintegrasi langsung dengan sistem autentikasi Django, sehingga pengembang tidak perlu membuat form login dari nol. Django juga sudah menangani aspek keamanan dasar seperti hashing password dan pengecekan status user. Selain itu, form ini cukup fleksibel untuk dikustomisasi, misalnya dengan menambahkan field baru atau mengubah tampilan input menggunakan `widgets`. Dukungan bawaan untuk bekerja dengan `LoginView` juga membuat implementasi login menjadi lebih cepat dan sederhana.

Namun, `AuthenticationForm` juga memiliki beberapa keterbatasan. Form ini hanya menyediakan `login` dengan `username` dan `password`, sehingga jika ingin mendukung login menggunakan email, nomor telepon, OTP, atau metode lain, developer perlu membuat custom form. Tampilan error message yang disediakan pun sangat standar dan sering kali perlu diubah agar lebih ramah bagi pengguna. Di luar itu, fitur tambahan seperti “remember me”, autentikasi dua faktor, atau captcha tidak tersedia secara default dan harus ditambahkan secara manual.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi dan otorisasi adalah dua konsep yang berbeda meskipun sering dipakai bersama dalam sistem keamanan aplikasi. Autentikasi merupakan proses memverifikasi identitas pengguna, misalnya dengan mencocokkan username dan password saat login untuk memastikan bahwa orang tersebut benar-benar pemilik akun. Setelah identitas pengguna terkonfirmasi, barulah masuk ke tahap otorisasi, yaitu menentukan apa saja yang boleh atau tidak boleh dilakukan pengguna tersebut di dalam sistem. Jadi, autentikasi menjawab pertanyaan “siapa kamu”, sedangkan otorisasi menjawab pertanyaan “apa yang boleh kamu lakukan”. Django mengimplementasikan keduanya melalui modul bawaan `django.contrib.auth`. Pada sisi autentikasi, Django menyediakan model User, fungsi `authenticate()` untuk memverifikasi kredensial, dan `login()` atau `logout()` untuk mengelola sesi pengguna. Sementara pada sisi otorisasi, Django menyediakan sistem permission dan group yang bisa diatur untuk setiap pengguna, serta dekorator atau mixin seperti `@login_required`, `@permission_required`, `LoginRequiredMixin`, dan `PermissionRequiredMixin` untuk membatasi akses ke view berdasarkan hak akses. Dengan begitu, Django memberi kerangka lengkap untuk memastikan hanya pengguna terverifikasi yang dapat masuk ke sistem, sekaligus mengatur apa saja yang bisa dilakukan sesuai dengan peran dan izinnya.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies memiliki kelebihan karena data disimpan langsung di browser pengguna sehingga bisa bertahan meskipun browser ditutup, serta tidak memerlukan penyimpanan tambahan di server. Cookies cocok digunakan untuk menyimpan preferensi ringan seperti bahasa, tema, atau opsi “remember me”. Namun, cookies memiliki keterbatasan ukuran (umumnya 4KB), ikut terkirim pada setiap request sehingga bisa menambah beban bandwidth, serta rentan terhadap serangan XSS jika tidak diamankan dengan benar. Karena data disimpan di sisi klien, cookies juga tidak ideal untuk informasi yang bersifat sensitif.

Sementara itu, session lebih aman karena data disimpan di server dan hanya session ID yang dikirimkan ke browser. Hal ini memungkinkan penyimpanan informasi sensitif seperti status login atau data pengguna dengan kapasitas yang lebih besar daripada cookies. Session juga tidak menambah beban request secara signifikan. Namun, penggunaan session membutuhkan resource server yang lebih besar, biasanya hanya berlaku selama browser aktif, dan bisa menimbulkan masalah saat aplikasi di-scale up jika tidak ada mekanisme session sharing antar server. Dengan demikian, cookies lebih cocok untuk preferensi pengguna yang ringan, sedangkan session lebih tepat digunakan untuk menyimpan state yang penting dan rahasia.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default, penggunaan cookies dalam pengembangan web tidak sepenuhnya aman karena ada sejumlah risiko potensial yang harus diwaspadai. Cookies bisa menjadi target serangan XSS (Cross-Site Scripting) jika dapat diakses melalui JavaScript, memungkinkan penyerang mencuri informasi sensitif. Selain itu, jika cookies dikirim melalui HTTP tanpa enkripsi, data dapat dengan mudah disadap oleh pihak ketiga. Risiko lain adalah CSRF (Cross-Site Request Forgery), karena cookies akan otomatis terkirim pada setiap permintaan ke server, sehingga penyerang bisa memanfaatkannya untuk mengirimkan request palsu. Untuk mengatasi hal ini, Django menyediakan beberapa mekanisme keamanan bawaan. Django memungkinkan pengaturan atribut HttpOnly agar cookies tidak bisa diakses lewat JavaScript, serta Secure untuk memastikan cookies hanya dikirim melalui HTTPS. Selain itu, Django mendukung konfigurasi SameSite untuk membatasi pengiriman cookies lintas situs, dan menyediakan opsi SESSION_COOKIE_SECURE serta CSRF_COOKIE_SECURE agar cookies sensitif hanya dikirim melalui koneksi terenkripsi. Django juga memiliki fitur signed cookies yang menggunakan secret key untuk memverifikasi integritas data sehingga cookies tidak bisa dimodifikasi secara sembarangan. Dengan kombinasi ini, Django membantu meningkatkan keamanan penggunaan cookies, meskipun pengembang tetap perlu mengaktifkan dan menyesuaikan pengaturan sesuai kebutuhan aplikasi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, aku bikin model Product di app products dan langsung aku hubungkan ke User pakai ForeignKey, jadi tiap produk pasti punya owner. Dengan begitu kalau user login, dia bisa lihat produk-produk miliknya sendiri lewat relasi user.products.all(). Setelah itu aku jalanin makemigrations dan migrate biar tabelnya kebentuk di database.

Lanjut ke fitur autentikasi, aku bikin view untuk register, login, dan logout. Buat register aku pakai UserCreationForm biar validasinya aman dan nggak perlu bikin dari nol. Setelah user berhasil daftar, aku langsung login-in dia otomatis dan bikin cookie last_login yang isinya waktu login terakhir. Cookie ini aku set pakai httponly biar nggak bisa diakses lewat JavaScript. Untuk login aku pakai AuthenticationForm, kalau berhasil masuk ya prosesnya mirip, langsung set cookie last_login. Logout tinggal panggil logout() bawaan Django dan aku sekalian hapus cookienya biar bersih.

Di halaman utama, aku cek dulu apakah user sudah login atau belum. Kalau sudah, aku tampilin username dan juga nilai dari cookie last_login yang tadi diset, plus aku juga munculin semua produk milik user itu. Kalau belum login, aku kasih pesan sederhana dan link ke halaman login atau register.

Supaya bisa dites bener-bener, aku bikin dua akun user lewat manage.py shell dan masing-masing aku tambahin tiga produk dummy. Jadi misalnya akun alice punya keyboard, mouse, monitor, sedangkan akun bob punya phone case, charger, sama earbuds. Dengan begitu pas login ke akun tertentu, yang muncul di homepage cuma produk dia sendiri.

Terakhir, aku tambahin beberapa setting buat ngamanin cookies dan session di settings.py. Di local development aku biarin SESSION_COOKIE_SECURE masih false karena belum pakai HTTPS, tapi kalau production nanti harus true. Aku juga set SESSION_COOKIE_HTTPONLY biar nggak bisa diakses lewat JavaScript dan kasih SameSite=Lax buat ngurangi risiko CSRF. Jadi alurnya rapi: user bisa daftar, login, lihat produknya sendiri, logout, dan semua itu sudah nyambung sama user di database plus ada cookies buat simpan last login.

</details>


<details align="justify">
    <summary><b>Tugas 5</b></summary>

Jika terdapat beberapa CSS selector yang diterapkan pada satu elemen HTML, browser akan menentukan prioritas berdasarkan tingkat spesifisitasnya. Urutan prioritas dimulai dari inline style yang ditulis langsung pada elemen, kemudian diikuti oleh selector dengan ID, selanjutnya class, attribute, dan pseudo-class, lalu yang paling rendah adalah selector tag atau pseudo-element. Jika terdapat aturan dengan tingkat spesifisitas yang sama, maka aturan yang ditulis paling akhir akan diambil.

Konsep responsive design sangat penting dalam pengembangan aplikasi web karena saat ini pengguna mengakses internet melalui berbagai perangkat dengan ukuran layar yang berbeda. Dengan responsive design, tampilan aplikasi dapat menyesuaikan ukuran layar sehingga tetap nyaman diakses baik di desktop, tablet, maupun smartphone. Sebagai contoh, Instagram Web sudah menerapkan responsive design karena tampilannya tetap rapi di berbagai perangkat, sedangkan beberapa situs web lama seperti portal sekolah atau instansi pemerintah seringkali belum responsive sehingga sulit diakses lewat perangkat mobile.

Margin, border, dan padding merupakan tiga hal yang berbeda dalam CSS box model. Margin adalah jarak di luar elemen yang memisahkannya dengan elemen lain di sekitarnya. Border adalah garis tepi yang mengelilingi elemen. Sedangkan padding adalah ruang di dalam elemen, yaitu antara konten dengan border. Ketiganya bisa diatur dengan properti CSS masing-masing, misalnya `margin: 20px;`, `border: 2px solid black;`, atau `padding: 10px;`. Analogi sederhananya seperti sebuah kardus: barang di dalam kardus adalah konten, ruang kosong di dalam kardus adalah padding, dinding kardus adalah border, dan ruang kosong di luar kardus adalah margin.

Flexbox dan grid layout merupakan dua teknik modern dalam CSS untuk mengatur tata letak. Flexbox berfungsi untuk mengatur layout dalam satu dimensi, entah secara horizontal (baris) maupun vertikal (kolom), sehingga mempermudah perataan dan distribusi elemen. Grid layout berbeda karena mendukung pengaturan dalam dua dimensi sekaligus (baris dan kolom) sehingga sangat cocok untuk tampilan yang lebih kompleks seperti dashboard atau galeri.

Proses implementasi checklist dilakukan secara bertahap. Pertama, saya membuat struktur HTML dasar untuk halaman seperti login dan register. Setelah itu, saya menambahkan CSS untuk memberikan warna, padding, margin, serta menata tombol. Selanjutnya, saya menggunakan flexbox untuk memusatkan form agar rapi di tengah halaman, serta grid untuk layout yang membutuhkan pembagian kolom. Checkbox kemudian diubah tampilannya agar lebih menarik, misalnya warna berubah menjadi kuning ketika dicentang. Setelah struktur dasar selesai, saya menambahkan responsivitas menggunakan media query bawaan Tailwind agar tampilan tetap menyesuaikan ukuran layar perangkat. Terakhir, saya melakukan pengujian di berbagai perangkat untuk memastikan semuanya berfungsi dengan baik.

</details>



