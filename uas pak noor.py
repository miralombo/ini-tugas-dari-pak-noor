import random

def play_game(level):
    # Tentukan rentang angka berdasarkan level (ditambah level 4-5 untuk variasi)
    if level == 1:
        min_num, max_num = 1, 10
        attempts = 5
    elif level == 2:
        min_num, max_num = 1, 50
        attempts = 7
    elif level == 3:
        min_num, max_num = 1, 100
        attempts = 10
    elif level == 4:
        min_num, max_num = 1, 500
        attempts = 12
    else:  # Level 5+
        min_num, max_num = 1, 1000
        attempts = 15
    
    # Generate angka acak
    target = random.randint(min_num, max_num)
    print(f"Selamat datang di Level {level}!")
    print(f"Saya telah memilih angka antara {min_num} dan {max_num}. Anda punya {attempts} kesempatan untuk menebak.")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Tebakan ke-{attempt}: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        
        if guess < target:
            print("Terlalu kecil!")
        elif guess > target:
            print("Terlalu besar!")
        else:
            print(f"Selamat! Anda menebak benar dalam {attempt} kali percobaan.")
            return True  # Menang
    
    print(f"Maaf, Anda kehabisan kesempatan. Angka yang benar adalah {target}.")
    return False  # Kalah

def main():
    level = 1
    score = 0  # Tambahan: sistem skor
    while True:
        won = play_game(level)
        if won:
            level += 1  # Naik level jika menang
            score += 10  # Tambah skor
            print(f"Anda naik ke Level {level}! Skor Anda: {score}")
        else:
            level = max(1, level - 1)  # Turun level jika kalah, tapi minimal level 1
            score = max(0, score - 5)  # Kurangi skor
        
        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            print(f"Terima kasih telah bermain! Skor akhir Anda: {score}")
            break

if __name__ == "__main__":
    main()