"""No missing module docstring"""

from lab_4 import *

def run_all():  # Шаг 9
    """Последовательно вызывает все функции."""
    print("Шаг 1")
    add(60,50)
    divide(10,5)

    print("\nШаг 2")
    subtract(10,6)

    print("\nШаг 3")
    multiply(6000,6)

    print("\nШаг 4")
    calculate_area(5,10)
    safe_divide(16,4)
    validate_age(99)

    print("\nШаг 5")
    generate_exception(-6)

    print("\nШаг 7")
    validate_input(-6)

    print("\nШаг 8")
    calculate_square_root(3)
    convert_to_integer(10.5)
    calculate_discount(100,20)

if __name__ == '__main__':
    run_all()
