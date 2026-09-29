skor = 0
nyawa = 1
nomor_soal = 1

while nomor_soal <= 3 and nyawa > 0:

    percobaan = 0
    benar = False

    # SOAL 1
    if nomor_soal == 1:

        while percobaan < 3:

            jawaban = input(
                "\n1. Hewan yang dijuluki raja hutan? "
            )

            if jawaban.lower() == "singa":
                print("Benar ✅")
                skor += 1
                benar = True
                break

            else:
                percobaan += 1
                print("Salah ❌")
                print("Percobaan:", percobaan, "/ 3")


    # SOAL 2
    elif nomor_soal == 2:

        while percobaan < 3:

            jawaban = input(
                "\n2. Ibukota Indonesia? "
            )

            if jawaban.lower() == "jakarta":
                print("Benar ✅")
                skor += 1
                benar = True
                break

            else:
                percobaan += 1
                print("Salah ❌")
                print("Percobaan:", percobaan, "/ 3")


    # SOAL 3
    elif nomor_soal == 3:

        while percobaan < 3:

            jawaban = input(
                "\n3. Berapa hasil 5 + 5? "
            )

            if jawaban == "10":
                print("Benar ✅")
                skor += 1
                benar = True
                break

            else:
                percobaan += 1
                print("Salah ❌")
                print("Percobaan:", percobaan, "/ 3")


    # Kalau gagal 3 kali
    if benar == False:
        nyawa -= 1
        print("Kesempatan habis ❌")
        print("Nyawa berkurang!")

    print("Skor:", skor)
    print("Nyawa:", nyawa)

    nomor_soal += 1


print("\n=== QUIZ SELESAI ===")
print("Skor akhir:", skor)

if nyawa == 0:
    print("Game Over 💀")
else:
    print("Selamat 🎉")