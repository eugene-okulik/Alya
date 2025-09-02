def operation_manager(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')

    return wrapper

@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        if second == 0:
            return "Ошибка: деление на ноль"
        return first / second
    elif operation == '*':
        return first * second
    else:
        return "Некорректная операция"

def main():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: необходимо ввести числовое значение.")
        return

    result = calc(num1, num2, None)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
