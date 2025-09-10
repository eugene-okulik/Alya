from dataclasses import dataclass, field
from typing import List, Optional


# Общий класс для всех цветов
@dataclass
class Flower:
    name: str
    color: str
    length_stem: float  # в сантиметрах
    freshness: int    # от 1 (не очень свежий) до 10 (очень свежий)
    price: float      # стоимость одного цветка
    lifespan: int     # среднее время жизни в днях

    def __str__(self):
        return (
            f"{self.name} ({self.color}), стебель: {self.length_stem}см, "
            f"свежесть: {self.freshness}, цена: {self.price}₽, "
            f"срок жизни: {self.lifespan} дн"
        )


# Подклассы для конкретных видов цветов
class Rose(Flower):
    def __init__(self, color, length_stem, freshness, price, lifespan):
        super().__init__('Роза', color, length_stem, freshness, price, lifespan)


class Tulip(Flower):
    def __init__(self, color, length_stem, freshness, price, lifespan):
        super().__init__('Тюльпан', color, length_stem, freshness, price, lifespan)


class Sunflower(Flower):
    def __init__(self, color, length_stem, freshness, price, lifespan):
        super().__init__('Подсолнечник', color, length_stem, freshness, price, lifespan)


# Класс букета
@dataclass
class Bouquet:
    flowers: List[Flower] = field(default_factory=list)

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)

    def total_cost(self) -> float:
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self) -> float:
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def days_until_wilt(self) -> float:
        """Определяет среднее время увядания цветов в букете"""
        return self.average_lifespan()

    def sort_by(self, parameter: str):
        """Сортирует цветы по указанному параметру"""
        valid_params = {
            'freshness': lambda f: f.freshness,
            'color': lambda f: f.color,
            'length_stem': lambda f: f.length_stem,
            'price': lambda f: f.price,
            'lifespan': lambda f: f.lifespan
        }
        key_func = valid_params.get(parameter)
        if key_func:
            self.flowers.sort(key=key_func)
        else:
            print(f"Недопустимый параметр сортировки: {parameter}")

    def find_by_parameter(self, parameter: str, value):
        """Поиск цветов по параметру"""
        valid_params = {
            'freshness': lambda f: f.freshness,
            'color': lambda f: f.color,
            'length_stem': lambda f: f.length_stem,
            'price': lambda f: f.price,
            'lifespan': lambda f: f.lifespan
        }
        key_func = valid_params.get(parameter)
        if not key_func:
            print(f"Недопустимый параметр поиска: {parameter}")
            return []

        return [flower for flower in self.flowers if key_func(flower) == value]

    def __str__(self):
        return '\n'.join(str(flower) for flower in self.flowers)


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляры цветов
    rose1 = Rose(color='красная', length_stem=50, freshness=8, price=300, lifespan=7)
    tulip1 = Tulip(color='жёлтый', length_stem=40, freshness=7, price=150, lifespan=5)
    sunflower1 = Sunflower(color='жёлтый', length_stem=70, freshness=9, price=200, lifespan=10)

    # Создаем букет и добавляем цветы
    bouquet = Bouquet()
    bouquet.add_flower(rose1)
    bouquet.add_flower(tulip1)
    bouquet.add_flower(sunflower1)

    # Выводим букет
    print("Букет:")
    print(bouquet)

    # Общая стоимость
    print(f"\nОбщая стоимость букета: {bouquet.total_cost()} ₽")

    # Время увядания
    print(f"\nСреднее время увядания: {bouquet.days_until_wilt()} дней")

    # Сортировка по свежести
    bouquet.sort_by('freshness')
    print("\nБукет отсортирован по свежести:")
    print(bouquet)

    # Сортировка по цвету
    bouquet.sort_by('color')
    print("\nБукет отсортирован по цвету:")
    print(bouquet)

    # Сортировка по длине стебля
    bouquet.sort_by('length_stem')
    print("\nБукет отсортирован по длине стебля:")
    print(bouquet)

    # Сортировка по цене
    bouquet.sort_by('price')
    print("\nБукет отсортирован по цене:")
    print(bouquet)

    # Поиск по цвету
    yellow_flowers = bouquet.find_by_parameter('color', 'жёлтый')
    print("\nЦветы жёлтого цвета:")
    for flower in yellow_flowers:
        print(flower)

    # Поиск по среднему времени жизни
    lifespan_7 = bouquet.find_by_parameter('lifespan', 7)
    print("\nСреднее время жизни:")
    for flower in lifespan_7:
        print(flower)
