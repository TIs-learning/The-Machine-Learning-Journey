import numpy as np
import os
os.system('cls')
b = np.array([1, 2, 4]) # Kita bisa membuat lebih dari 1 dimensi 2/3/4... ; Perhatikan tanda kurung
# 1. Contoh 2 dimensi
c = np.array([[1, 3, 5, 9], 
              [7, 8, 9, 8], 
              [1, 8, 6, 5],
              [13, 14, 15, 2]]) # Selalu perhatikan kurung siku

# 2. contoh 3 dimensi
d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
              [[28, 29, 30], [31, 32, 33], [34, 35, 36]]])
# cara mengakses chain indexing
print(d[0][0][0])
# Cara mengakses multidimensional indexing
print(d[0, 0, 0])
# 1 = baris, 2 = kolom, 3 = elemen

#slicing: print(d[start:end:step])
print("Slicing: ")
print(c[1:3]) # Pemilihan Semua baris
print(c[1:3, 1:3]) # Kiri = baris , Kanan = kolom, bisa juga pake rumus slicing
# Bisa di cek disini
# print(d.ndim)

# Operasi Scalar 
# ini kayak operasi aritmatika nilai tunggal dalam matriks/array, bisa : +, -, :, *, **  

# Fungsi Vektor: ini 1 dimensi, ada yang mencari akar, nilai pi, dll

# Broadcasting: ini kayak perkalian matriks
# syaratnya: ukuran dimensinya sama persis, atau salah satu ukuran dimensinya 1

# fungsi agregasi: print(np.mean(namavar)), bisa: mean,min,median,max,argmin/max,std,var,sum,dll kalo ada
# argminmax buat mengetahui index angka terbesar/kecil
# print(np.sum(namavar, axis=0)) 0 berlaku ke semuanya, 1 berlaku perbaris

# filtering: andai ada matriks umur = np.array([....])
# tua = umur[umur > 40]
# tua = umur[(umur > 40) & (kondisi ke 2)] bisa juga kayak gini
# bisa juga ayam = np.where(age>18, ages, 0) ke 1 kondisi, 2 itu arraynya, 3 nilai pengisi
# apapun yang tidak sesuai dengan kondisi akan diganti dengan nilai pengisi

# random number: a = np.random.default_rng() bisa ditambah seed= , bisa dipanggil dengan print(a.integers(1, 7)) ; 1 sampai 6 maksudnya, bisa ditulis low = high=
# bisa juga ditambah 1 parameter size = .., untuk seberapa banyk, bisa juga size nya dibikin baris dan kolom supaya jadi matriks
# size=(3, 4). default_rng bisa diganti uniform jika mau desimal dengan parameter sama
# fungsi acak array: rng.shuffle(nama array), rng.choice(namavariable) buat milih bisa ditambah size dan jadi matriks.


