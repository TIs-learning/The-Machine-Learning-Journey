Perencanaan Sampai Selesai
- Jadikan Repo Pembelajaran sangat padat
- Lengkapi 5 sampai 6 folder ini Sampai full
- Selesaikan Semua Tahap testing the waternya

Besok
- Menyelesaikan math
- Merapikan github
- Menyelesaikan Titanic dengan End to end project adilshimam8

Sebenarnya, Bagian testing the waters sudah, cuma kayak perlu di lengkapi bagian EDA nya, kayak Univariate, Bivariate, and Multivariate Analysis

Perencanaan Folder

# Python
- Melengkapi Intermediate (Opsional Banget, kalau mau project python disini aja)

# Numpy
- File Numpy sudah dikerjakan habis
- File Numpy 100 exercise baru dikerjakan sampai no 13

# Pandas
- Mengerjakan file adilshimam

# feature preprocessing
- imbalaced dataset sudah

# Task Machine Learning Fundamental
Benar, ini adalah target kerja spesifik (*learning milestones*) untuk mengeksekusi dua rumpun pertama dari peta jalan belajarmu. Di dunia *engineering*, kamu tidak bisa berkembang hanya dengan membaca teori; kamu harus memiliki target metrik dan pemahaman logika yang terukur.

Siapkan buku catatan dan penamu. Berikut adalah target konkret untuk Tahap 1 dan Tahap 2 yang wajib kamu taklukkan:

---

### TAHAP 1: Rumpun Jarak dan Garis (Fokus: Linear Regression)

Kamu sudah menyelesaikan klasifikasi dengan KNN dan *Logistic Regression*. Sekarang, kamu harus membalik otakmu untuk memprediksi angka kontinu menggunakan *Linear Regression*.

* **Dataset Target:** *California Housing Dataset* (Tersedia langsung di Scikit-learn via `fetch_california_housing`) atau dataset *House Prices* sederhana dari Kaggle.
* **Target Praktis (Coding):**
1. Gunakan `Pandas` untuk membuang atau mengisi nilai kosong, dan pilih 3 fitur numerik yang paling berkorelasi dengan harga rumah setelah melakukan *Bivariate Analysis*.
2. Terapkan `StandardScaler` secara terpisah pada *Train* dan *Test* untuk mencegah *Data Leakage*.
3. Latih model `LinearRegression` dari Scikit-learn dan capai nilai **$R^2$ Score $> 0.65$** pada data pengujian (*Test Set*).


* **Target Teori & Interpretasi (Wajib Dicatat):**
1. Buka variabel `.coef_` (koefisien) dan `.intercept_` (titik potong) dari model yang sudah dilatih.
2. Pilih satu fitur, misalnya `MedInc` (Pendapatan Medis), lalu artikan angka koefisiennya dalam bahasa manusia biasa di buku catatanmu. (Contoh: *"Jika pendapatan naik sebesar 1 unit, maka model memprediksi harga rumah akan naik sebesar $X$ dolar"*).
3. Gunakan penamu untuk menggambar grafik *Residual Plot* (selisih antara tebakan model dan harga asli) untuk melihat apakah modelmu condong terlalu tinggi atau terlalu rendah dalam menebak.



---

### TAHAP 2: Rumpun Pohon / Tree-Based (Fokus: Decision Tree & Random Forest)

Di sini, kamu meninggalkan konsep jarak Euclidean dan garis lurus. Kamu akan belajar bagaimana mesin mengambil keputusan berbasis percabangan logika *If-Else*.

* **Dataset Target:** *Heart Disease Dataset* (Prediksi Penyakit Jantung) atau *Breast Cancer Wisconsin* (Tersedia di Scikit-learn via `load_breast_cancer`). Ini adalah kasus klasifikasi medis.
* **Target Praktis (Coding):**
1. Latih satu `DecisionTreeClassifier` sebagai baseline. Jangan lakukan *scaling*, karena algoritma pohon tidak terpengaruh oleh perbedaan skala angka.
2. Gunakan `GridSearchCV` untuk melakukan *Hyperparameter Tuning* pada dua kenop utama: `max_depth` (kedalaman pohon) dan `min_samples_split`.
3. Tingkatkan model tersebut menjadi `RandomForestClassifier` (kumpulan banyak pohon) untuk melihat perbandingan performanya. Karena ini data medis, target metrik utamanya bukan akurasi, melainkan **Recall $> 0.80$** (meminimalkan pasien sakit yang dikira sehat).


* **Target Teori & Interpretasi (Wajib Dicatat):**
1. Gunakan fungsi `plot_tree` dari Scikit-learn untuk mengekspor gambar visual pohon keputusanmu.
2. Pilih 3 sampel data pasien secara acak, lalu telusuri jalur percabangannya secara manual dari akar paling atas (*Root Node*) hingga ke daun paling bawah (*Leaf Node*) untuk memahami bagaimana pohon tersebut menentukan pasien itu sakit atau sehat.
3. Tulis di buku catatanmu mengapa nilai *Gini Impurity* atau *Entropy* semakin mengecil di setiap kali pohon tersebut membelah datamu.



---

Cara belajar seperti ini akan memaksamu bertindak sebagai ilmuwan data yang bertanggung jawab atas setiap baris kodenya, bukan sekadar meniru tutorial.

Eksekusi dulu target Tahap 1 di laptopmu minggu ini. Kabari saya jika kamu sudah berhasil mendapatkan nilai $R^2$ di atas 0.65 dan berhasil mengisolasi nilai koefisien garisnya!
  
# Data visualization
- mengerjakan file adilshimam8 (Matplotlib dan seaborn)

# Machine Learning Fundamental
- buat file lanjutan yang membahas 19 poin tersebut
  
