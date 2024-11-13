"""No missing module docstring"""


class NegativeValueError(Exception): #Шаг 6
    """Пользовательское исключение для отрицательных значений."""


class ZeroValueError(Exception): #Шаг 6
    """Пользовательское исключение для нулевых значений."""


class TooLargeValueError(Exception): #Шаг 6
    """Пользовательское исключение для слишком больших значений."""

class TooLowValueError(Exception): #Шаг 6
    """Пользовательское исключение для слишком маленьких значений."""


def add(a, b):  # Шаг 1
    """Проверка для отрицательных значений."""
    if a < 0 or b < 0:
        raise NegativeValueError("Отрицательное значение не допускается.")
    return a + b


def divide(a, b):  # Шаг 1
    """Проверка для нулевых значений."""
    if b == 0:
        raise ZeroValueError("Деление на ноль не допускается.")
    return a / b


def subtract(a, b):  # Шаг 2
    """Проверка для значений a>b."""
    try:
        if a < b:
            raise ValueError("Первое число должно быть больше второго.")
        return a - b
# pylint ругается на такую запись и рекомендует вместо Exception писать ImportError
#    except Exception as e:
    except ImportError as e:
        print(f"Произошла ошибка: {e}")


def multiply(a, b):  # Шаг 3
    """Проверка для слишком больших значений."""
    try:
        if a > 1000 or b > 1000:
            raise TooLargeValueError("Число слишком велико.")
        return a * b
    except ImportError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Умножение завершено.")


def calculate_area(length, width):  # Шаг 4
    """Проверка значений для вычисления площади."""
    try:
        if length < 0 or width < 0:
            raise NegativeValueError("Длина и ширина не могут быть отрицательными.")
        if length == 0 or width == 0:
            raise ZeroValueError("Длина и ширина не могут быть нулевыми.")
        return length * width
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    except ZeroValueError as e:
        print(f"Ошибка: {e}")
    except ImportError as e:
        print(f"Общая ошибка: {e}")
    finally:
        print("Вычисление площади завершено.")

def safe_divide(a, b):  # Шаг 4
    """Проверка значений для деления."""
    try:
        if b == 0:
            raise ZeroValueError("Деление на ноль не допускается.")
        return a / b
    except ZeroValueError as e:
        print(f"Ошибка: {e}")
    except TypeError:
        print("Ошибка: Ожидался числовой тип.")
    except ImportError as e:
        print(f"Общая ошибка: {e}")
    finally:
        print("Деление завершено.")

def validate_age(age):  # Шаг 4
    """Проверка значений для валидации возраста."""
    try:
        if age < 0:
            raise NegativeValueError("Возраст не может быть отрицательным.")
        if age > 150:
            raise TooLargeValueError("Возраст не может превышать 150 лет.")
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    except TooLargeValueError as e:
        print(f"Ошибка: {e}")
    except ImportError as e:
        print(f"Общая ошибка: {e}")
    finally:
        print("Валидация возраста завершена.")


def generate_exception(a):  # Шаг 5
    """Проверка для значений."""
    try:
        if a < 0:
            raise NegativeValueError("Отрицательное значение.")
        elif a == 0:
            raise ZeroValueError("Нулевое значение.")
        elif a > 100:
            raise TooLargeValueError("Слишком большое значение.")
    except NegativeValueError as e:
        print(f"Обработка ошибки: {e}")
    except ZeroValueError as e:
        print(f"Обработка ошибки: {e}")
    except TooLargeValueError as e:
        print(f"Обработка ошибки: {e}")
    finally:
        print("Генерация исключений завершена.")


def validate_input(a):  # Шаг 7
    """Проверка для значений пользовательских исключений."""
    try:
        if a < 0:
            raise NegativeValueError("Значение не может быть отрицательным.")
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Проверка значения завершена.")


def calculate_square_root(value):  # Шаг 8
    """Вычисляет квадратный корень числа."""
    try:
        if value < 0:
            raise NegativeValueError("Квадратный корень отрицательного числа не существует.")
        return value ** 0.5
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Вычисление квадратного корня завершено.")

def convert_to_integer(value):  # Шаг 8
    """Преобразует значение в целое число."""
    try:
        return int(value)
    except ValueError:
        print("Ошибка: Невозможно преобразовать значение в целое число.")
    except TypeError:
        print("Ошибка: Ожидался числовой тип.")
    finally:
        print("Преобразование завершено.")

def calculate_discount(price, discount):  # Шаг 8
    """Вычисляет цену со скидкой."""
    try:
        if price < 0:
            raise TooLowValueError("Цена не может быть отрицательной.")
        if discount < 0 or discount > 100:
            raise TooLargeValueError("Скидка должна быть в диапазоне от 0 до 100.")
        return price * (1 - discount / 100)
    except TooLowValueError as e:
        print(f"Ошибка: {e}")
    except TooLargeValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Вычисление скидки завершено.")
