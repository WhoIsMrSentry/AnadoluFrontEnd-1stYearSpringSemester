# MARK: - Dikdörtgen Sınıfı

class Rectangle:
    """Dikdörtgen: alan ve çevre hesaplama"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Alanı hesapla"""
        return self.width * self.height
    
    def perimeter(self):
        """Çevreyi hesapla"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Dikdörtgen({self.width}x{self.height}) - Alan: {self.area()}, Çevre: {self.perimeter()}"


# Test
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(rect)
    print(f"Alan: {rect.area()}")
    print(f"Çevre: {rect.perimeter()}")
