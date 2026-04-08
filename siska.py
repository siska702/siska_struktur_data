nama = "Siska Andini Utami"
data = list(nama.upper())
data.sort()
print("Data setelah diurutkan:", data)
cari = "A"
kiri = 0
kanan = len(data) - 1
ditemukan = False
while kiri <= kanan:
    tengah = (kiri + kanan) // 2

    if data[tengah] == cari:
        print("Huruf", cari, "ditemukan pada indeks ke-", tengah)
        ditemukan = True
        break
    elif data[tengah] < cari:
        kiri = tengah + 1
    else:
        kanan = tengah - 1

if not ditemukan:
    print("Huruf tidak ditemukan")