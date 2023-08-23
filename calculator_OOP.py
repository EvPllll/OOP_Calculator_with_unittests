class Calculator:
    """
    Класс калькулятор, имеющий стандартные функции:
    + сложение
    - вычитание
    * умножение
    / деление
    ** возведение в степень
    **0.5 квадратный корень
    % вычисление процента
    """

    def __init__(self):
        """
        Переменные (списки), записывающие историю операций и результаты
        """
        self.story = []
        self.results = []

    def summ(self, first_digit: [int, float], second_digit: [int, float]) -> [int, float]:
        """
        Функция сложения чисел
        :param first_digit: первое слагаемое
        :param second_digit: второе слагаемое
        :return: сумма

        >>> Calculator().summ(2, 2)
        4
        >>> Calculator().summ(41, 59)
        100
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргументы должны быть числами')
        else:
            result = first_digit + second_digit
            self.results.append(result)
            expression = f'{first_digit} + {second_digit} = {result}'
            self.story.append(expression)
            return result

    def difference(self, first_digit: [int, float], second_digit: [int, float]) -> [int, float]:
        """
        Функция вычитания второго числа из первого
        :param first_digit: уменьшаемое
        :param second_digit: вычитаемое
        :return: разность

        >>> Calculator().difference(2, 2)
        0
        >>> Calculator().difference(10, 20)
        -10
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргументы должны быть числами')
        else:
            result = first_digit - second_digit
            self.results.append(result)
            expression = f'{first_digit} - {second_digit} = {result}'
            self.story.append(expression)
            return result

    def multiply(self, first_digit: [int, float], second_digit: [int, float]) -> [int, float]:
        """
        Функция умножения чисел
        :param first_digit: первый множитель
        :param second_digit: второй множитель
        :return: произведение

        >>> Calculator().multiply(2, 2)
        4
        >>> Calculator().multiply(5, -4)
        -20
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргументы должны быть числами')
        else:
            result = first_digit * second_digit
            self.results.append(result)
            expression = f'{first_digit} * {second_digit} = {result}'
            self.story.append(expression)
            return result

    def divide(self, first_digit: [int, float], second_digit: [int, float]) -> [int, float]:
        """
        Функция деления первого числа на второе
        :param first_digit: делимое
        :param second_digit: делитель
        :return: частное

        >>> Calculator().divide(2, 2)
        1.0
        >>> Calculator().divide(100, 2)
        50.0
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргументы должны быть числами')
        else:
            result = first_digit / second_digit
            self.results.append(result)
            expression = f'{first_digit} / {second_digit} = {result}'
            self.story.append(expression)
            return result

    def exponentiation(self, first_digit: [int, float], second_digit: [int, float]) -> [int, float]:
        """
        Функция возведения первого числа в степень второго
        :param first_digit: основание
        :param second_digit: показатель
        :return: степень

        >>> Calculator().exponentiation(2, 3)
        8
        >>> Calculator().exponentiation(2, -3)
        0.125
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргументы должны быть числами')
        else:
            result = first_digit ** second_digit
            self.results.append(result)
            expression = f'{first_digit} ** {second_digit} = {result}'
            self.story.append(expression)
            return result

    def square_root(self, first_digit: [int, float], second_digit=0.5) -> [int, float]:
        """
        Функция, вычисляющая корень числа
        :param first_digit: число, корень которого следует вычислить
        :param second_digit: степень корня (по умолчанию 0.5 - квадратный корень)
        :return: корень

        >>> Calculator().square_root(121)
        11.0
        >>> Calculator().square_root(225)
        15.0
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргумент должны быть числом')
        else:
            result = first_digit ** second_digit
            self.results.append(result)
            expression = f'{first_digit} ** {second_digit} = {result}'
            self.story.append(expression)
            return result

    def percent(self, first_digit: [int, float], second_digit: int) -> [int, float]:
        """
        Вычисление процента первого числа по отношению ко второму
        :param first_digit: число, процент которого нужно вычислить
        :param second_digit: число, указывающее какой процент нужно вычислить
        :return: результат вычисления

        >>> Calculator().percent(50, 50)
        25.0
        >>> Calculator().percent(100, 30)
        30.0
        """
        if not isinstance(first_digit, int | float) and isinstance(second_digit, int | float):
            raise ValueError('Аргументы должны быть числами')
        else:
            result = first_digit / 100 * second_digit
            self.results.append(result)
            expression = f'{first_digit} / 100 * {second_digit} = {result}'
            self.story.append(expression)
            return result

    def show_results(self) -> list:
        """
        Вывод результатов операций
        :return: список с результатами операций
        """
        return self.results

    def show_story(self) -> list:
        """
        Вывод истории операций
        :return: список с историей операций
        """
        return self.story


if __name__ == '__main__':
    print(Calculator().summ(2, 2))  # Ответ: 4
    print(Calculator().difference(2, 2))  # Ответ: 0
    print(Calculator().multiply(2, 3))  # Ответ: 6
    print(Calculator().divide(2, 2))  # Ответ: 1.0
    print(Calculator().exponentiation(2, 3))  # Ответ: 8
    print(Calculator().square_root(4))  # Ответ: 2.0
    print(Calculator().percent(100, 50))  # Ответ: 50.0
