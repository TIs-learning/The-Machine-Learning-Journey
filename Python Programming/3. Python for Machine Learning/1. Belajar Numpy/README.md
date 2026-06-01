## Roadmap

Fase 1: Pengenalan & Pembuatan Array (Array Creation)
Fokus pertama adalah memahami apa itu ndarray (N-dimensional array) dan mengapa ini jauh lebih cepat daripada List bawaan Python.

Materi Utama:

  - Mengimpor NumPy (import numpy as np).
  - Membuat array dari List (np.array).
  - Memahami dimensi array (1D/Vektor, 2D/Matriks, 3D/Tensor).
  - Membuat array dengan fungsi bawaan: np.zeros(), np.ones(), np.arange(), np.linspace().
  - Membuat array dengan nilai acak (np.random).
  - Atribut penting untuk dicek: .shape, .ndim, .size, .dtype.

Fase 2: Indexing & Slicing (Mengakses Data)
Setelah bisa membuat array, Anda harus tahu cara mengambil data spesifik di dalamnya.

Materi Utama:

  - Indexing dasar di array 1D dan 2D (misal: arr[0, 1]).
  - Slicing berdasar rentang (misal: arr[1:3, :]).
  - Boolean Indexing / Masking: Mengambil data berdasarkan kondisi logika (Sangat penting!). Contoh: arr[arr > 5].
  - Fancy Indexing: Mengakses beberapa elemen sekaligus menggunakan list indeks.

Fase 3: Manipulasi Bentuk Array (Array Manipulation)
Di dunia nyata, data sering kali bentuknya tidak sesuai kebutuhan model Anda, jadi Anda harus bisa merombaknya.

Materi Utama:

  - Mengubah dimensi: .reshape() (misal mengubah array 1D berisi 9 elemen menjadi matriks 3x3).
  - Meratakan array: .flatten() atau .ravel() (mengubah 2D/3D kembali ke 1D).
  - Memutar matriks (Transpose): .T atau np.transpose().
  - Menggabungkan array (Concatenation): np.vstack() (vertikal), np.hstack() (horizontal), dan np.concatenate().

Fase 4: Operasi Matematika & Konsep "Broadcasting"
Ini adalah letak kekuatan utama NumPy. Anda tidak perlu menggunakan for loop untuk menghitung setiap elemen matematika.

Materi Utama:

  - Operasi Element-wise: Tambah, kurang, kali, bagi secara langsung antar array (arr1 + arr2).
  - Universal Functions (ufuncs): np.sqrt(), np.exp(), np.sin(), np.log().
  - Broadcasting: Ini adalah konsep paling krusial! Memahami bagaimana NumPy menjumlahkan matriks besar dengan array kecil (misal: matriks        3x3 ditambah array 1D berisi 3 elemen).

Fase 5: Statistik & Agregasi
Digunakan untuk meringkas dan mendapatkan insight awal dari data numerik Anda.

Materi Utama:

  - Fungsi dasar: np.sum(), np.mean(), np.median(), np.max(), np.min(), np.std().
  - Memahami parameter axis:
    - axis=0 (menghitung nilai per kolom / secara vertikal).
    - axis=1 (menghitung nilai per baris / secara horizontal).
  - Mencari indeks dari nilai terbesar/terkecil: np.argmax() dan np.argmin().

Fase 6: Aljabar Linear Dasar (Linear Algebra)
Jika Anda tertarik masuk ke ranah Machine Learning atau Deep Learning, aljabar linear adalah pondasinya.

Materi Utama:

  - Perkalian titik (Dot Product) vs Perkalian Matriks (Matrix Multiplication): np.dot() atau menggunakan operator @.
  - Modul np.linalg:
    - Mencari determinan matriks (np.linalg.det).
    - Mencari invers matriks (np.linalg.inv).
    - Mencari eigenvalues dan eigenvectors.
   
Fase 7: Latihan & Proyek Mini (Tugas Praktik)
Teori saja tidak cukup. Coba kerjakan proyek kecil-kecilan ini tanpa menggunakan Pandas:

  - Normalisasi Data: Buat array 2D berisi data acak, lalu normalisasi datanya (kurangi setiap nilai dengan rata-rata kolom, lalu bagi dengan   standar deviasinya).

  - Manipulasi Gambar Sederhana: Baca file gambar dengan Matplotlib (plt.imread), gambar akan terbaca sebagai array 3D NumPy (Tinggi x Lebar     x RGB). Coba konversi gambar tersebut menjadi hitam putih dengan merata-ratakan nilai RGB-nya menggunakan NumPy!
