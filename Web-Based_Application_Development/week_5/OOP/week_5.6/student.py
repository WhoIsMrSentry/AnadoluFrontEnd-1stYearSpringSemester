# MARK: - Öğrenci Sınıfı

class Student:
    """Öğrenci: vize ve final notu, ortalama hesapla"""
    
    def __init__(self, name, midterm, final):
        self.name = name
        self.midterm = midterm
        self.final = final
    
    def average(self):
        """Ortalamayı hesapla: vize %40 + final %60"""
        return (self.midterm * 0.4) + (self.final * 0.6)
    
    def __str__(self):
        return f"{self.name}: Vize={self.midterm}, Final={self.final}, Ort={self.average():.2f}"


# Test
if __name__ == "__main__":
    student = Student("Ahmet", 70, 85)
    print(student)
    print(f"Ortalama: {student.average():.2f}")
