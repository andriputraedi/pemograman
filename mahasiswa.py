print("Andri Putraedi")

print("Program Menghitung Nilai Mahasiswa")

nama=input("Masukan Nama :")
nim=input("Masukan NIM   :")
matkul=input("Masukan Mata Kuliah :")
smtr=input("Masukan Semester      :")
prs=float(input("Masukan Nilai Presensi :"))
tugas=float(input("Masukan Nilai Tugas :"))
quiz=float(input("Masukan Nilai QUIZE :"))
prtk=float(input("Masukan Nilai Pratikum :"))
uts=float(input("Masukan Nilai UTS:"))
uas=float(input("Masukan Nilai UAS:"))

na=(prs * 0.1) + (tugas * 0.3) + (quiz * 0.1) + (prtk * 0.2) + (uts * 0.1) + (uas * 0.2)

print("============ HASIL AKHIR ============")

print("Nama  :",nama)
print("NIM   :",nim)
print("Mata Kuliah :",matkul)
print("Semester    :",smtr)
print("Presensi :", prs)
print("Nilai Tugas    :", tugas)
print("Nilai QUIZE :",quiz)
print("Nilai Pratikum :",prtk)
print("Nilai UTS   :",uts)
print("Nilai UAS   :", uas)
print("Nilai Akhir :",na)

nilai_relatif = ""
bobot = ""
if na >= 81 and na <= 100:
    nilai_relatif = "A"
    bobot = "4"
elif na >= 76 and na <= 80.9:
    nilai_relatif = "B+"
    bobot = "3.5"
elif na >= 66 and na<= 75.9:
    nilai_relatif = "B"
    bobot = "3"
elif na >= 61 and na <=65.9:
    nilai_relatif = "C+"
    bobot = "2.5"
elif na >= 51 and na <=60.9:
    nilai_relatif = "C"
    bobot = "2"
elif na >= 26 and na <= 50.9:
    nilai_relatif = "D"
    bobot = "1"
elif na >= 0 and na <= 25.9:
    nilai_relatif = "E"
    bobot = "0"
else: 
    nilai_relatif = "Tidak Valid"
status = ""
if nilai_relatif == "A" or nilai_relatif == "B+" or nilai_relatif == "B" or nilai_relatif == "C+" or nilai_relatif == "C" :
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print("NILAI RELATIF :", nilai_relatif)
print("STATUS :",status)
print("BOBOT  :", bobot)