nama = input("Nama: ")
n_harian = float(input("Nilai Harian: "))
n_uts = float(input("Nilai UTS: "))
n_uas = float(input("Nilai UAS: "))

nilaiAkhir = n_harian + n_uts + n_uas

print("=============================")
print(f"Nama:", nama)
print(f"Nilai Harian:", n_harian)
print(f"Nilai UTS:", n_uts)
print(f"Nilai UAS:", n_uas)
print(f"Rata-Rata:", float(nilaiAkhir))

if nilaiAkhir >= 80:
    print("Predikat A")
elif nilaiAkhir >= 70:
    print("Predikat B")
elif nilaiAkhir >= 60:
    print("Predikat C")
elif nilaiAkhir >= 50:
    print("Predikat D")
elif nilaiAkhir < 50:
    print("Predikat D")