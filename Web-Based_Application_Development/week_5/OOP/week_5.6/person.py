# MARK: - Kişi Sınıfı

class Person:
    """Kişi: ad ve telefon numarası"""
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} - {self.phone}"


# Test
if __name__ == "__main__":
    person = Person("Ali", "0555123456")
    print(person)
