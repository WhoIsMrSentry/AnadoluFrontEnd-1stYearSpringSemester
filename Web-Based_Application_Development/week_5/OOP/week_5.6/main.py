# MARK: - Ana Program: Record Listesi

from record import Record


def main():
    """3 Record nesnesi oluştur, listeye ekle ve yazdır"""
    
    # MARK: - Record Nesneleri Oluştur
    records = []
    
    # from_line ile oluştur
    records.append(Record.from_line("1|Ahmet|0555111111"))
    records.append(Record.from_line("2|Zeynep|0555222222"))
    records.append(Record.from_line("3|Ali|0555333333"))
    
    # MARK: - Listeyi Yazdır
    print("=" * 40)
    print("KAYITLAR")
    print("=" * 40)
    
    for record in records:
        print(record)
    
    print("=" * 40)
    print(f"Toplam kayıt: {len(records)}")


if __name__ == "__main__":
    main()
