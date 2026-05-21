# 📘 Bab 1: Memberi Komputer Kemampuan untuk Belajar dari Data

**Bab 1 tidak berisi contoh kode apa pun.**

---

## 🐍 Menginstal Python

Python tersedia untuk tiga sistem operasi utama: **Windows, macOS, dan Linux**.
Silakan unduh installer resmi di:

👉 [https://www.python.org](https://www.python.org)

Buku ini ditulis untuk Python versi:

```
>= 3.7.0
```

Disarankan menggunakan versi Python 3 terbaru. Sebagian besar kode masih kompatibel dengan Python lama, termasuk:

```
>= 2.7.10
```

Namun, jika menggunakan Python 2.7, pastikan memahami perbedaan utamanya:

👉 [https://wiki.python.org/moin/Python2orPython3](https://wiki.python.org/moin/Python2orPython3)

---

### 🔎 Cek Versi Python

Gunakan perintah berikut di terminal:

```bash
python -V
```

Contoh output:

```bash
Python 3.7.1 :: Continuum Analytics, Inc.
```

---

## 📦 Pip (Package Manager)

`pip` adalah package manager bawaan Python (sejak versi 3.3).

Dokumentasi resmi:
👉 [https://docs.python.org/3/installing/index.html](https://docs.python.org/3/installing/index.html)

### Install package

```bash
pip install SomePackage
```

Contoh:

```bash
pip install numpy pandas matplotlib scikit-learn
```

### Update package

```bash
pip install SomePackage --upgrade
```

---

## 🐍 Anaconda (Rekomendasi untuk Data Science)

Anaconda adalah distribusi Python yang sangat cocok untuk:

* Data Science
* Machine Learning
* Komputasi ilmiah

Download di:
👉 [https://docs.anaconda.com/anaconda/install/](https://docs.anaconda.com/anaconda/install/)

Panduan:
👉 [https://docs.anaconda.com/anaconda/user-guide/getting-started/](https://docs.anaconda.com/anaconda/user-guide/getting-started/)

### Install package dengan conda

```bash
conda install SomePackage
```

### Update package

```bash
conda update SomePackage
```

---

## 📚 Library yang Digunakan

Dalam buku ini kita akan menggunakan:

* **NumPy** → manipulasi array multidimensi
* **pandas** → pengolahan data tabular
* **matplotlib** → visualisasi data

---

## ⚙️ Paket Inti

* [NumPy](http://www.numpy.org) >= 1.17.4
* [SciPy](http://www.scipy.org) >= 1.3.1
* [scikit-learn](http://scikit-learn.org/stable/) >= 0.22.0
* [matplotlib](http://matplotlib.org) >= 3.1.0
* [pandas](http://pandas.pydata.org) >= 0.25.3

---

## 📓 Jupyter Notebook

File dengan ekstensi `.ipynb` adalah **Jupyter Notebook**.

Kelebihan Jupyter:

* Menggabungkan kode + output + visualisasi + dokumentasi
* Mendukung Markdown & LaTeX
* Sangat cocok untuk analisis data

---

### Install Jupyter

#### Dengan pip

```bash
pip install notebook
```

#### Dengan conda

```bash
conda install notebook
```

---

### Menjalankan Jupyter

Masuk ke folder project:

```bash
cd ~/kode/buku-machine-learning
```

Lalu jalankan:

```bash
jupyter notebook
```

Akan terbuka di browser:

```
http://localhost:8888/
```
---

### Referensi Jupyter

* [https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)
* [https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html)

---

## 🚀 JupyterLab (Alternatif Modern)

JupyterLab adalah versi lebih modern dari Jupyter Notebook.

### Install

```bash
conda install -c conda-forge jupyterlab
```

### Menjalankan

```bash
jupyter lab
```

Dokumentasi resmi:
👉 [https://jupyterlab.readthedocs.io/en/stable/](https://jupyterlab.readthedocs.io/en/stable/)

---

## 📝 Catatan

* "IPython Notebook" sekarang dikenal sebagai **Jupyter Notebook**
* Jupyter mendukung banyak bahasa selain Python (R, Julia, dll)
