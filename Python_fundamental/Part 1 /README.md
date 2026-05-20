## Bab 1: Memberi Komputer Kemampuan untuk Belajar dari Data

**Bab 1 tidak berisi contoh kode apa pun.**

Plt.savet(gambar/06_05.png, dpi=300)

## Menginstal paket Python

Python tersedia untuk ketiga sistem operasi utama — Microsoft Windows, macOS, dan Linux — dan penginstal, serta dokumentasinya, dapat diunduh dari situs web resmi Python: https://www.python.org.

Buku ini ditulis untuk Python versi`>= 3.7.0`, dan direkomendasikan
Anda menggunakan Python 3 versi terbaru yang tersedia saat ini,
meskipun sebagian besar contoh kode mungkin juga kompatibel dengan versi lama Python 3 dan Python`>= 2.7.10`. Jika Anda memutuskan untuk menggunakan Python 2.7 untuk mengeksekusi contoh kode, pastikan Anda mengetahui perbedaan utama antara kedua versi Python. Ringkasan bagus tentang perbedaan antara Python 3 dan 2.7 dapat ditemukan di https://wiki.python.org/moin/Python2orPython3.

**Catatan**

Anda dapat memeriksa versi default Python Anda saat ini dengan menjalankan

$ ular python -V

Dalam kasus saya, itu kembali

Python 3.7.1 :: Continuum Analytics, Inc.


#### Pip

Paket tambahan yang akan kita gunakan di seluruh buku ini dapat diinstal melalui program penginstal`pip`, yang telah menjadi bagian dari pustaka standar Python sejak Python 3.3. Informasi lebih lanjut tentang pip dapat ditemukan di https://docs.python.org/3/installing/index.html.

Setelah kita berhasil menginstal Python, kita dapat menjalankan pip dari terminal baris perintah untuk menginstal paket Python tambahan:

pip instal SomePackage


(dengan`SomePackage`sebagai pengganti numpy, pandas, matplotlib, scikit-learn, dan sebagainya).

Paket yang sudah terinstal dapat diperbarui melalui flag`--upgrade`:

pip instal SomePackage --upgrade


#### AnakondaDistribusi Python alternatif yang sangat direkomendasikan untuk komputasi ilmiah
adalah Anaconda oleh Continuum Analytics. Anaconda adalah distribusi Python gratis—termasuk penggunaan komersial—yang siap untuk perusahaan yang menggabungkan semua paket Python penting untuk ilmu data, matematika, dan teknik dalam satu distribusi lintas platform yang mudah digunakan. Penginstal Anaconda dapat diunduh di https://docs.anaconda.com/anaconda/install/, dan panduan memulai cepat Anaconda tersedia di https://docs.anaconda.com/anaconda/user-guide/getting-started/.

Setelah berhasil menginstal Anaconda, kita dapat menginstal paket Python baru menggunakan perintah berikut:

conda menginstal SomePackage

Paket yang ada dapat diperbarui menggunakan perintah berikut:

conda perbarui SomePackage

Sepanjang buku ini, kita terutama akan menggunakan array multidimensi NumPy untuk menyimpan dan memanipulasi data. Kadang-kadang, kita akan menggunakan pandas, yang merupakan perpustakaan yang dibangun di atas NumPy yang menyediakan alat manipulasi data tingkat tinggi tambahan yang membuat bekerja dengan data tabular menjadi lebih nyaman. Untuk menambah pengalaman belajar kita dan memvisualisasikan data kuantitatif, yang seringkali sangat berguna untuk memahaminya secara intuitif, kita akan menggunakan perpustakaan matplotlib yang sangat dapat disesuaikan.

#### Paket inti

8. Film yang berhubungan dengan acara TV

- [NumPy](http://www.numpy.org) >= 1.17.4
- [SciPy](http://www.scipy.org) >= 1.3.1
- [scikit-learn](http://scikit-learn.org/stable/) >= 0.22.0
- [matplotlib](http://matplotlib.org) >= 3.1.0
- [pandas](http://pandas.pydata.org) >= 0.25.3

## Buku Catatan Python/JupyterBeberapa pembaca bertanya-tanya tentang`.ipynb`dari file kode -- file ini adalah notebook IPython. Saya memilih notebook IPython daripada skrip`.py`Python biasa, karena menurut saya skrip tersebut sangat bagus untuk proyek analisis data! Notebook IPython memungkinkan kita memiliki semuanya di satu tempat: Kode kita, hasil dari eksekusi kode, plot data kita, dan dokumentasi yang mendukung Markdown yang praktis dan sintaksis LaTeX yang kuat!

![](./images/ipynb_ex1.png)

**Catatan Tambahan:** "IPython Notebook" baru-baru ini menjadi "[Jupyter Notebook](<http://jupyter.org>)"; Jupyter adalah proyek payung yang bertujuan untuk mendukung bahasa lain selain Python termasuk Julia, R, dan banyak lagi. Namun jangan khawatir, untuk pengguna Python, hanya ada perbedaan dalam terminologi (sekarang kami mengatakan "Jupyter Notebook" dan bukan "IPython Notebook").

Notebook Jupyter dapat diinstal seperti biasa melalui pip.

$ pip instal buku catatan jupyter

Alternatifnya, kita dapat menggunakan penginstal Conda jika kita menginstal Anaconda atau Miniconda:

$ conda instal buku catatan jupyter

Untuk membuka notebook Jupyter, kami`cd`ke direktori yang berisi contoh kode Anda, misalnya.
    $ cd ~/kode/buku-mesin-pembelajaran python

dan luncurkan`jupyter notebook`dengan mengeksekusi

$buku catatan jupyter

Jupyter akan dimulai di browser default kami (biasanya berjalan di [http://localhost:8888/](http://localhost:8888/)). Sekarang, kita cukup memilih notebook yang ingin Anda buka dari menu Jupyter.

![](./images/ipynb_ex2.png)

Untuk informasi selengkapnya tentang notebook Jupyter, saya merekomendasikan [Panduan Pemula Jupyter](http://jupyter-notebook-beginner-guide.readthedocs.org/en/latest/what_is_jupyter.html) dan [Dasar-Dasar Notebook Jupyter](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).

## Lab Jupyter Alternatif untuk Jupyter Notebook, yang disebut Jupyter Lab, dirilis pada tahun 2018. Ia beroperasi dengan jenis file`.ipynb`yang sama tetapi menawarkan beberapa fitur tambahan di antarmuka browser. Apakah Anda menggunakan Jupyter Notebook atau Jupyter Lab adalah masalah preferensi, namun

Jupyter Lab dapat diinstal melalui

$ conda install -c conda-forge jupyterlab
    
dan mirip dengan memulai Jupyter Notebooks, Anda dapat menjalankan perintah

$ laboratorium jupyter
    
di terminal baris perintah Anda untuk meluncurkan sesi Jupyter Lab di browser Anda. Untuk informasi lebih lanjut tentang proyek Jupyter Lab, silakan kunjungi dokumentasi resmi di https://jupyterlab.readthedocs.io/en/stable/,
