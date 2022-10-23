#input nilai variable
a = input("Masukan Nilai A: ")
b = input("Masukan Nilai B: ")

#cetak nilai variable
print("Variable A: ",a)
print("Variable B: ",b)

#cetak hasil kedua operasi variable dengan string format
print("Hasil Penggabungan {1} & {0} : ".format(a,b) + str(a)+str(b))

#konversi nilai variable
a = int(a);
b = int(b);

print("Hasil Penjumlahan {1} + {0} : %d".format(a,b) %(a+b))
print("Hasil Penjumlahan {1} / {0} : %d".format(a,b) %(a/b))
