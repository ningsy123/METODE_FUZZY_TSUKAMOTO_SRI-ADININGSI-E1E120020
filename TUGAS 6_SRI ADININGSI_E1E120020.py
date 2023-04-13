import numpy as np
import matplotlib.pyplot as plt
import math

print('NAMA \t: SRI ADININGSI')
print('NIM \t: E1E120020')
print('PROGRAM MODEL FUZZY TSUKAMOTO ')


def permintaan_sedikit(minta):
    if minta <= x1:
        return 1.0
    elif minta >= x2:
        return 0.0
    else:
        return (x2 - minta) / (x2-x1)


def permintaan_banyak(minta):
    if minta <= x1:
        return 0.0
    elif minta >= x2:
        return 1.0
    else:
        return (minta - x1) / (x2-x1)


def persediaan_sedikit(sedia):
    if sedia <= y1:
        return 1.0
    elif sedia >= y2:
        return 0.0
    else:
        return (y2 - sedia) / (y2-y1)


def persediaan_banyak(sedia):
    if sedia <= y1:
        return 0.0
    elif sedia >= y2:
        return 1.0
    else:
        return (sedia - y1) / (y2-y1)


def produksi_brg_minimal(produksi):
    if produksi <= z1:
        return 1.0
    elif produksi >= z2:
        return 0.0
    else:
        return (z2 - produksi) / (z2-z1)


def produksi_brg_maksimal(produksi):
    if produksi <= z1:
        return 0.0
    elif produksi >= z2:
        return 1.0
    else:
        return (produksi - z1) / (z2-z1)


print('\nSoal : ')
x1 = float(input('Masukkan Permintaan Terkecil = '))
x2 = float(input('Masukkan Permintaan Terbesar = '))
y1 = float(input('Masukkan Persediaan Terkecil  = '))
y2 = float(input('Masukkan Persediaan Tebesar = '))
z1 = float(input('Masukkan Produksi Barang Minimal = '))
z2 = float(input('Masukkan Produksi Barang Maksimal = '))

print('\nPertanyaan : ')
minta = float(input('Masukkan  Jumlah Permintaan = '))
sedia = float(input('Masukkan Jumlah Persediaan = '))

# permintaan turun
print('Nilai derajat keanggotaan permintaan sedikit = ', permintaan_sedikit(minta))
x = np.linspace(0, 5000+50, 10000)
y = [permintaan_sedikit(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Turun')
if minta < 0 or minta > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = permintaan_sedikit(minta)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axvline(x=minta, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
####################

# permintaan naik
print('Nilai derajat keanggotaan permintaan naik = ', permintaan_banyak(minta))
x = np.linspace(0, x2+50, 10000)
y = [permintaan_banyak(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Naik')
if minta < 0 or minta > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = permintaan_banyak(minta)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Derajat Keanggotaan')
    plt.title('Fungsi Keanggotaan Permintaan Naik dan Turun')
    plt.axvline(x=minta, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
plt.show()
####################

# persediaan turun
print('Nilai derajat keanggotaan persediaan turun = ', persediaan_sedikit(sedia))
x = np.linspace(0, y2+50, 10000)
y = [persediaan_sedikit(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Turun')
if sedia < 0 or sedia > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = persediaan_sedikit(sedia)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axvline(x=sedia, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
#############

# persediaan naik
print('Nilai derajat keanggotaan persediaan naik = ', persediaan_banyak(sedia))
x = np.linspace(0, 600+50, 10000)
y = [persediaan_banyak(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Naik')
if sedia < 0 or sedia > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = persediaan_banyak(sedia)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Derajat Keanggotaan')
    plt.title('Fungsi Keanggotaan Persediaan Terkecil dan Terbanyak')
    plt.axvline(x=sedia, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
plt.show()
####################

# Produksi barang turun
x = np.linspace(0, 7000+50, 10000)
y = [produksi_brg_minimal(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.plot(x, y)

# Produksi barang naik
x = np.linspace(0, 7000+50, 10000)
y = [produksi_brg_maksimal(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Derajat Keanggotaan')
plt.title('Fungsi Keanggotaan Produksi Barang Turun dan Naik')
plt.plot(x, y)
plt.show()

print('\nRule-->Min :')
print('[R1] IF Permintaan BANYAK And Persediaan BANYAK THEN Produksi Barang BERTAMBAH')
nilai_min1 = min(permintaan_banyak(minta), persediaan_banyak(sedia))
print('(', '', permintaan_banyak(minta), ',', '', persediaan_banyak(sedia), ')')
print("Nilai minimum adalah", nilai_min1)

print('\n[R2] IF Permintaan SEDIKIT And Persediaan SEDIKIT THEN Produksi Barang BERKURANG')
nilai_min2 = min(permintaan_sedikit(minta), persediaan_sedikit(sedia))
print('(', '', permintaan_sedikit(minta), ',', '', persediaan_sedikit(sedia), ')')
print("Nilai minimum adalah", nilai_min2)

print('[R3] IF Permintaan SEDIKIT And Persediaan BANYAK THEN Produksi Barang BERKURANG')
nilai_min3 = min(permintaan_sedikit(minta), persediaan_banyak(sedia))
print('(', '', permintaan_sedikit(minta), ',', '', persediaan_banyak(sedia), ')')
print("Nilai minimum adalah", nilai_min3)

print('\n[R4] IF Permintaan BANYAK And Persediaan SEDIKIT THEN Produksi Barang BERTAMBAH')
nilai_min4 = min(permintaan_banyak(minta), persediaan_sedikit(sedia))
print('(', '', permintaan_banyak(minta), ',', '', persediaan_sedikit(sedia), ')')
print("Nilai minimum adalah", nilai_min4)

print('\nHimpunan Produksi Barang : ')
print('[R1]==>Himpunan Produksi Bertambah')
a1 = ((nilai_min1 * (z2-z1))+z1)
print(a1)

print('\n[R2]==>Himpunan Produksi Bertambah')
a2 = ((nilai_min2 * (z2-z1))+z1)
print(a2)

print('\n[R3]==>Himpunan Produksi Berkurang')
a3 = (z2 - (nilai_min3 * (z2-z1)))
print(a3)

print('\n[R4]==>Himpunan Produksi Berkurang')
a4 = (z2 - (nilai_min4 * (z2-z1)))
print(a4)

print('\nMenghitung Z akhir dengan rata-rata z berbobot : ')
Z = ((nilai_min1*a1)+(nilai_min2*a2)+(nilai_min3*a3)+(nilai_min4*a4)) / \
    (nilai_min1+nilai_min2+nilai_min3+nilai_min4)
print(Z)
print("Jadi, jumlah jenis makanan yang harus diproduksi = ", round(Z))
