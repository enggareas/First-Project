import random
pilihan = input("Apa pilihanmu? ").strip().lower()
komputer = random.choice(["batu", "gunting", "kertas"])
print("Komputer memilih", komputer)

if pilihan == komputer:
    print("Seri")
elif pilihan == "batu" and komputer == "gunting":
    print("Kamu menang")
elif pilihan == "kertas" and komputer == "batu":
    print("Kamu menang")
elif pilihan == "gunting" and komputer == "kertas":
    print("Kamu menang")
elif pilihan == "batu" and komputer == "kertas":
    print("Kamu kalah")
elif pilihan == "kertas" and komputer == "gunting":
    print("Kamu kalah")
elif pilihan == "gunting" and komputer == "batu":
    print("Kamu kalah")

else:
    print("Pilihan tidak valid")