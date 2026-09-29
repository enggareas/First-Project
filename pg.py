skor = 0
nyawa = 2

pilihan = input("1. Ikan bernafas menggunakan...\na.Insang\nb.Paru-paru\nc.Hidung\n")

if pilihan == "a" or pilihan == "A":
    print("Jawaban Benar")
    skor = skor + 2
else:
    print("Jawaban Salah")
    skor = skor - 1
    nyawa = nyawa - 1

print("\nSkor kamu, ", skor)
print("Nyawa ", nyawa)

pilihan = input("\n2. Ibukota Jawa Tengah...\na.Bandung\nb.Surabaya\nc.Semarang\n")

if pilihan == "c" or pilihan == "C":
    print("Jawaban Benar")
    skor = skor + 2
else:
    print("Jawaban Salah")
    skor = skor - 1
    nyawa = nyawa - 1

print("\nSkor kamu, ", skor)
print("Nyawa ", nyawa)

if nyawa == 0:
    print("\nGame Over")
else:
    print("\nQuiz Selesai")

print("Skor AKhir: ", skor)       