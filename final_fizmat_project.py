#Подписан формулы, некоторые действия и точные значения км, миль и тд.тп.

class Fraction:
    def __init__(self, numerator, denominator):
        # Ввод дроби с проверкой знаменателя
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулём")
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator
        # Получение значения числителя

    def get_denominator(self):
        return self.denominator
        # Получение значения знаменателя

    def add(self, other):
        # Сложение дробей: a/b + c/d = (ad + bc)/bd
        n1 = self.numerator * other.denominator + other.numerator * self.denominator #n1 и n2 - новые, получившиеся после операций числитель и знаменатель
        n2 = self.denominator * other.denominator
        return Fraction(n1, n2)

    def subtract(self, other):
        # Вычитание дробей: a/b - c/d = (ad - bc)/bd
        n1 = self.numerator * other.denominator - other.numerator * self.denominator
        n2 = self.denominator * other.denominator
        return Fraction(n1, n2)

    def multiply(self, other):
        # Умножение дробей: a/b * c/d = ac/bd
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        # Деление дробей: a/b / c/d = ad/bc
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        # Строковое представление дроби
        return f"{self.numerator}/{self.denominator}"


class TemperatureConverter:
    @staticmethod #Прочитал, что можно использовать @staticmethod для того, чтобы не создавать объекты класса и вызывать метод напрямую через класс, так как подобные методы - просто утилита
    def celsius_to_fahrenheit(celsius):
        # Формула перевода Цельсии в Фаренгейт: (C × 9/5) + 32
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        # Формула перевода Фаренгейта в Цельсию: (F - 32) × 5/9
        return (fahrenheit - 32) * 5 / 9


class MetricConverter:
    @staticmethod
    def km_to_miles(km):
        # 1 километр = 0.621371 мили
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles):
        # 1 миля = 1.60934 километра
        return miles * 1.60934

    @staticmethod
    def liters_to_gallons(liters):
        # 1 литр = 0.264172 галлона
        return liters * 0.264172

    @staticmethod
    def gallons_to_liters(gallons):
        # 1 галлон = 3.78541 литра
        return gallons * 3.78541


# Примеры использования
f1 = Fraction(5, 6)
f2 = Fraction(9, 3)
print(f1.multiply(f2))
print(f1.add(f2))

print(TemperatureConverter.celsius_to_fahrenheit(10))
print(TemperatureConverter.fahrenheit_to_celsius(45))
print(MetricConverter.km_to_miles(45))
print(MetricConverter.gallons_to_liters(10))