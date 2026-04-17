def int_input(prompt):
    """Get integer input from user with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")


def metin_input(prompt):
    """Get text input from user."""
    return input(prompt)


def gorevleri_oku_finally(dosya_adi="gorevler.txt"):
    """Read tasks from file."""
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    finally:
        print("Dosya işlemi tamamlandı.")


def gorev_ekle(gorev, dosya_adi="gorevler.txt"):
    """Add a new task to file."""
    with open(dosya_adi, 'a', encoding='utf-8') as f:
        f.write(gorev + "\n")


def gorev_ara(anahtar, dosya_adi="gorevler.txt"):
    """Search for tasks containing keyword."""
    gorevler = gorevleri_oku_finally(dosya_adi)
    return [g for g in gorevler if anahtar.lower() in g.lower()]


def gorev_sil(index, dosya_adi="gorevler.txt"):
    """Delete task at given index."""
    gorevler = gorevleri_oku_finally(dosya_adi)
    if 0 <= index < len(gorevler):
        gorevler.pop(index)
        with open(dosya_adi, 'w', encoding='utf-8') as f:
            f.writelines(gorevler)
        return True
    return False


def next_id(dosya_adi="gorevler.txt"):
    """Get next available ID."""
    gorevler = gorevleri_oku_finally(dosya_adi)
    return len(gorevler) + 1