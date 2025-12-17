# Program Piramida Sederhana

karakter = input("Masukkan karakter: ")
tinggi = int(input("Masukkan tinggi piramida: "))

for i in range(1, tinggi + 1):
    # spasi di kiri
    print(" " * (tinggi - i), end="")
    # karakter piramida
    print(karakter * (2 * i - 1))
