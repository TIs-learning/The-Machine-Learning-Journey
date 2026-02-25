import pandas as pd
import numpy as np
import os
os.system('cls')

''' imbalance dataset tidak sama dengan distrbusi yang tidak rata/skewed'''

# Definisikan jumlah dan rasio perbandingan antar kelas
n_samples = 1000 # Pembagian banyaknya jumlah sample secara keseluruhan
n_ratio = 0.9 # Penyusunan ratio kelas 0 dan kelas 1

# Logika pembagian kelas
ini_class_0 = int(n_samples * n_ratio) # kelas 0 mendapatkan 900
ini_class_1 = n_samples - ini_class_0 # kelas 1 hanya mendapat sisanya yaitu 100
print(f'Nilai kelas 0 adalah {ini_class_0}, Dan nilai kelas 1 adalah {ini_class_1}')

# membuat angka acak berdasarkan kelas ke 0
n_random = np.random.seed(90)
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=ini_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=ini_class_0),
    'target': [0] * ini_class_0
})

# membuat angka acak berdasarkan kelas ke 1
class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=ini_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=ini_class_1),
    'target': [1] * ini_class_1
})

#print(class_0)
#print()
#print(class_1)

'''
Cara Penanganan nya ada 2:
- Pengambilan Sampling Naik,
- Pengambilan Sampling Turun

1. Pengambilan Sampling Naik (Upsampling): mencopy (duplikat) data/kelas yang sedikit(minoritas) secara random berulang-ulang agar 
                                           jumlahnya setidaknya sama dengan yang banyak(dalam kasus ini yang 900/kelas 0)
efek: Model akan mengalami Overfitting, tapi tetap dianjurkan supaya model setidaknya tidak hanya menebak asal karena kelas
      rendah dan juga sebagai dasar pembelajaran algoritma yang lebih advance seperti SMOTE
2. Pengambilan Sampling Turun (Downsampling): mengurangi (menghapus) data/kelas yang mayoritas agar jumlahnya sama dengan
                                            kelas minoritas
efek: Model akan menjadi terlalu sederhana karena bisa jadi dari data yang dihapus tersebut terdapat pola/informasi penting
      yang bisa dipelajari oleh model, kelemahannya tidak bisa mencari pola kompleks, atau dengan kata lain terkena underfitting
'''
# Var df didefinisikan sebagai gabungan class 0 dan kelas 1
df=pd.concat([class_0,class_1]).reset_index(drop=True)
#print(df.head())

# membagi data
df_mayoritas = df[df['target']== 1]
df_minoritas = df[df['target']== 0]

# Import library dari sklearn
from sklearn.utils import resample

# Upsampling kelas minoritas (kelas 1)
minoritas_upsampled = resample(class_1, 
                               replace=True, # Ini penting banget (True) biar datanya bisa diduplikat/diambil ulang
                               n_samples=len(class_0), # Kita samain jumlahnya dengan kelas mayoritas (class_0)
                               random_state=42) # Biar hasil acaknya tetep sama kalau kodenya di-run ulang

# Gabungin class_0 sama data class_1 yang udah di-upsample tadi
df_upsampled = pd.concat([class_0, minoritas_upsampled]).reset_index(drop=True) 
print(f'ini adalah: \n{df_upsampled['target'].value_counts()}') # jumlah nya sudah sama

# Downsampling kelas mayoritas (kelas 0)
mayoritas_downsampled = resample(class_0, 
                                 replace=False, # Perhatiin ini jadi False, soalnya kita cuma mau milih sebagian data tanpa diduplikat
                                 n_samples=len(class_1), # Kita turunin jumlahnya biar sama kayak kelas minoritas (class_1)
                                 random_state=42)

df_downsampled = pd.concat([mayoritas_downsampled, class_1]).reset_index(drop=True)
print(f'Ini kedua: \n{df_downsampled}') # jumlah data/kelasnya 200
print(f'Ini buat cek yang kedua: \n{df_downsampled['target'].value_counts()}') # dengan masing masing 100