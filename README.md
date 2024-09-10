# ✧˚ ༘ ⋆｡♡˚💐 ***Selamat Datang di Effendy Bouquet*** 💐 ✧˚ ༘ ⋆｡♡˚
<img src="pict/effendy_bouquet.jpg" width="600" height="200">

## Tugas Individu 2 PBP 
### Cara Mengimplementasikan Sesuai _Checklist_
Untuk memulai proyek Django, saya pertama-tama membuat direktori utama dengan nama ```effendy-bouquet``` kemudian menghubungkan repositori lokal dengan repositori di GitHub dan melakukan _cloning_ repositori tersebut ke komputer lokal. Di dalam direktori ini, saya membuat virtual environment menggunakan perintah ```python -m venv env```. Virtual environment ini berguna untuk mengisolasi package dan dependencies proyek, sehingga tidak akan bentrok dengan proyek lain atau sistem Python global. Setelah itu, saya mengaktifkan virtual environment dengan menjalankan ```env\Scripts\activate```.
Kemudian membuat file ```requirements.txt```. Setelah itu menginstalasi _dependencies_ dengan pip ```pip install -r requirements.txt```. Dengan Django terinstal, saya membuat proyek baru dengan nama effendy_bouquet menggunakan perintah ```django-admin startproject effendy_boquet .```.  Dilanjutkan dengan mengubah ```ALLOWED_HOSTS``` di ```settings.py``` untuk keperluan deployment pada direktori ```effendy_bouquet```. Setelah proyek dibuat, saya menjalankan server lokal dengan ```python manage.py runserver``` untuk memastikan bahwa semuanya berjalan dengan baik. Saya kemudian memeriksa aplikasi melalui browser dengan mengakses ```http://localhost:8000```. Setelah memastikan bahwa semuanya berjalan lancar, saya menghentikan server dengan ```Ctrl+C``` dan menonaktifkan virtual environment menggunakan perintah ```deactivate```.


Langkah berikutnya adalah memulai repositori Git untuk proyek saya. Saya melakukan inisialisasi direktori lokal sebagai repositori Git dengan perintah git init. Kemudian, saya membuat file .gitignore untuk mengecualikan file yang tidak perlu dilacak oleh Git, seperti file sementara dan direktori virtual environment. Setelah menyiapkan file ```.gitignore```, saya menambahkan semua file ke repositori dengan ```git add .```, menyimpan perubahan dengan ```git commit -m "Initial commit"```, dan akhirnya mengirimkan berkas ke repositori GitHub menggunakan perintah ```git push```.
Setelah mengatur repositori Git, saya mengaktifkan kembali virtual environment dan membuat aplikasi baru dengan nama ```main``` menggunakan perintah ```python manage.py startapp main```. Saya menambahkan aplikasi main ke dalam daftar ```INSTALLED_APPS``` di file ```settings.py``` proyek, sehingga aplikasi ini terintegrasi dengan proyek utama.


Kemudian, saya mendefinisikan model Product di file ```models.py``` aplikasi ```main```. Model ini memiliki atribut ```name, price, description dan quantity``` yang akan digunakan untuk menyimpan data produk. Setelah membuat model, saya menjalankan perintah ```python manage.py makemigrations``` untuk membuat file migrasi, diikuti dengan ```python manage.py migrate``` untuk menerapkan perubahan ke database.


Selanjutnya, saya membuat template HTML di folder ```templates/main/``` dengan nama ```main.html```, yang berfungsi untuk menampilkan data dari views. Di file ```views.py``` saya mendefinisikan fungsi main yang mengirimkan nama aplikasi, nama saya, dan kelas ke template ```main.html```. Saya memastikan bahwa fungsi ini terintegrasi dengan model jika diperlukan.
Untuk routing, saya mengonfigurasi file ```urls.py``` di aplikasi main untuk mengarahkan URL ke fungsi view main. Saya juga menambahkan routing di file ```urls.py``` proyek utama untuk memastikan bahwa aplikasi main dapat diakses melalui root URL. Setelah semua konfigurasi selesai, saya menjalankan server Django lagi dan memeriksa aplikasi di browser melalui ```localhost``` untuk memastikan bahwa semuanya berfungsi dengan baik.
Terakhir, saya mengikuti petunjuk dari platform PWS untuk melakukan deployment aplikasi. Saya menambahkan URL deployment ke dalam daftar ```ALLOWED_HOSTS``` di file ```settings.py``` dan melakukan push ke PWS mengikuti petunjuk yang diberikan. 

### Bagan yang Berisi _Request Client_ ke Web Aplikasi Berbasis Django Beserta Responnya
<img src="pict/bagan.png" width="800" height="500">

Berikut ini adalah deskripsi dari masing-masing langkah dalam alur tersebut:
1.	```Client Request```:Proses dimulai ketika seorang pengguna atau client mengirimkan request ke server melalui browser. Misalnya, mereka mengetikkan URL seperti ```http://example.com/products/```. Request ini berisi informasi tentang URL yang ingin diakses oleh pengguna.
2.	```urls.py```:  Setelah request diterima oleh server, Django pertama kali memeriksa file ```urls.py```. Di sini, Django akan mencocokkan URL yang diminta dengan pola-pola yang telah didefinisikan di ```urls.py```. Setiap URL dipetakan ke fungsi view tertentu. Setelah pola URL yang sesuai ditemukan, request tersebut kemudian diarahkan ke fungsi view yang tepat di views.py.
3.	```views.py```: Fungsi view di ```views.py``` bertanggung jawab untuk menangani logika yang dibutuhkan dalam menanggapi request pengguna. Pada tahap ini, ```views.py``` bisa memproses data yang sudah ada, atau jika diperlukan, ia akan meminta data dari basis data melalui ```models.py```. View juga menentukan data apa yang akan disampaikan ke template untuk ditampilkan ke pengguna.
4.	```models.py```: Jika fungsi view di ```views.py``` membutuhkan data dari basis data, maka ia akan berinteraksi dengan ```models.py```. Model berfungsi sebagai representasi struktur data dan logika bisnis yang berhubungan dengan data tersebut. Dalam ```models.py```, Django akan mengambil atau menyimpan data ke basis data sesuai dengan permintaan view. Setelah data yang dibutuhkan diperoleh, data tersebut akan diteruskan kembali ke ```views.py```.
5.	```Template (HTML)```: Setelah data dikumpulkan atau diproses oleh ```views.py```, langkah selanjutnya adalah mengirim data tersebut ke template. ```Template``` adalah berkas HTML yang telah disiapkan untuk menampilkan data yang diterima dari view. Django mengisi template dengan data yang telah diproses, lalu menghasilkan halaman ```HTML``` yang siap untuk ditampilkan kepada pengguna.
6.	```Response to Client```: Setelah template diisi dengan data yang sesuai, Django mengonversi template menjadi halaman HTML yang lengkap. Halaman HTML ini kemudian dikirim sebagai response kembali ke browser pengguna. Pengguna akan melihat hasil akhir di browser mereka, sesuai dengan data yang telah dikirim dari server.

### Fungsi Git dalam Pengembangan Perangkat Lunak
Git adalah alat penting dalam pengembangan perangkat lunak yang membantu melacak perubahan kode, memungkinkan kerja sama tim, dan menjaga backup dari setiap versi proyek. Dengan Git, pengembang bisa bekerja bersama tanpa saling mengganggu karena mereka bisa membuat cabang (branch) untuk fitur atau perbaikan tertentu. Setiap perubahan yang dibuat dapat dilacak, sehingga jika terjadi kesalahan mereka bisa kembali ke versi sebelumnya. Git juga memastikan transparansi, di mana semua anggota tim bisa melihat siapa yang membuat perubahan dan kapan perubahan itu dilakukan.

### Alasan Framework Django dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

Django adalah framework yang kuat karena ditulis dengan Python, bahasa pemrograman yang mudah dipahami. Python mendukung portabilitas, multi-paradigma, dan memiliki sifat interaktif yang membuat pengembang lebih fokus pada penyelesaian masalah, bukan sekadar sintaksis.

Django dikenal aman digunakan karena fitur keamanan internalnya yang selalu diperbarui, melindungi aplikasi web dari serangan seperti SQL injection dan _cross-site scripting_. Selain itu, Django menyederhanakan proses pengembangan dengan fitur-fitur bawaan seperti URL routing, otentikasi pengguna, dan migrasi skema database. Django juga menganut konsep _KISS (Keep It Short and Simple)_ dan _DRY (Don’t Repeat Yourself)_, yang berarti pengembang harus menulis kode dengan singkat dan jelas, tanpa pengulangan yang tidak perlu.

Framework ini fleksibel dan dapat digunakan untuk proyek kecil hingga besar, serta mendukung lintas platform seperti mobile, komputer, dan tablet. Django juga memiliki template engine bawaan, tapi tetap kompatibel dengan template lain seperti Jinja2. Keunggulan lainnya, Django sudah digunakan secara luas oleh perusahaan besar, pemerintah, dan organisasi di seluruh dunia, baik untuk manajemen konten, sosial media, hingga proyek komputasi ilmiah.

### Alasana Model pada Django disebut Sebagai _ORM_

Django memiliki _Object Relational Mapping (ORM)_ bawaan yang memudahkan pengembang melakukan query database tanpa menulis banyak kode. ORM ini memungkinkan pengembang bekerja dengan database menggunakan objek Python, tanpa perlu menulis query SQL secara langsung. Setiap field dalam class ORM dapat langsung diubah menjadi tabel di database. Dengan ORM, pengembang dapat melakukan operasi ```CRUD (Create, Read, Update, Delete)``` dengan metode berbasis objek, yang mempermudah integrasi antara kode Python dan sistem basis data relasional. Django juga didukung dengan dokumentasi yang lengkap dan jelas, sehingga mudah dipahami bahkan oleh pemula.


