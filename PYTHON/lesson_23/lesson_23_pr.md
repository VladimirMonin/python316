## Практика по абстрактным классам и Mixin

### Цели практики:

- Понять и применить абстрактные классы и методы.
- Освоить наследование и работу с Mixin.
- Изучить порядок разрешения методов (MRO).

### Краткое содержание:

Студентам предлагается создать архитектуру классов для интернет-магазина электроники. Они начнут с абстрактного
класса `Product`, который будет наследоваться конкретными продуктами, такими как `Smartphone` и `Laptop`. Для добавления
специфичных характеристик к этим продуктам будут использоваться Mixin, такие как `FragileMixin` и `BulkyItemMixin`.

### Классы и методы:

1. **Абстрактный класс `Product`**:
    - Атрибуты: `name` (название продукта), `price` (цена).
    - Абстрактный метод: `get_description()` – возвращает описание продукта.

2. **Конкретные классы `Smartphone` и `Laptop`**:
    - Наследуются от `Product`.
    - Имеют дополнительные атрибуты, например, `battery_life` для `Smartphone` и `weight` для `Laptop`.
    - Реализуют метод `get_description()`.

3. **Mixin `FragileMixin` и `BulkyItemMixin`**:
    - `FragileMixin` добавляет метод `packaging_instructions()`, возвращающий инструкции по упаковке хрупкого товара.
    - `BulkyItemMixin` добавляет метод `shipping_instructions()`, возвращающий инструкции по доставке крупногабаритного
      товара.

### Порядок подмешивания Mixin:

Mixin должны быть подмешаны таким образом, чтобы они не нарушали основную логику класса-потомка и не вызывали конфликты
между методами. Обычно Mixin указывают перед основным классом в списке наследования.

Пример:

```python
class Smartphone(Product, FragileMixin):
    pass


class Laptop(Product, BulkyItemMixin):
    pass
```

### Инициализаторы:

Все классы должны корректно инициализировать атрибуты через `__init__`. Mixin могут добавлять свои атрибуты, если это
требуется, но главное – не забыть инициализировать атрибуты базовых классов.

Пример:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class FragileMixin:
    def packaging_instructions(self):
        return "Use bubble wrap."


class Smartphone(Product, FragileMixin):
    def __init__(self, name, price, battery_life):
        super().__init__(name, price)
        self.battery_life = battery_life
```

### Критерии проверки:

- Корректность определения абстрактных классов и методов.
- Правильное наследование классов и применение Mixin.
- Понимание и правильное использование порядка разрешения методов (MRO).
- Атрибуты и методы должны быть инициализированы и реализованы согласно заданию.

