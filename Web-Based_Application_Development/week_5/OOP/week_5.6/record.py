# MARK: - Record Sınıfı

class Record:
    """Kayıt: ID, ad, telefon"""
    
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
    
    @classmethod
    def from_line(cls, line):
        """Satırdan nesne oluştur: "3|Ali|0555" → Record(3, "Ali", "0555")"""
        parts = line.strip().split("|")
        return cls(int(parts[0]), parts[1], parts[2])
    
    def __str__(self):
        return f"Record({self.id}, {self.name}, {self.phone})"


# Test
if __name__ == "__main__":
    record = Record.from_line("3|Ali|0555123456")
    print(record)
