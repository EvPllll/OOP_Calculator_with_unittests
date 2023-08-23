import calculator_OOP
from calculator_OOP import Calculator

import doctest
from unittest import TestCase


def load_tests(loader, tests, ignore):
    """
    Импорт doctest в unittests
    :param tests: Параметр теста для добавления нужных doctest
    :return: Возвращает результат doctest
    """
    tests.addTests(doctest.DocTestSuite(calculator_OOP))
    return tests


class CalculatorTest(TestCase):
    """
    Класс unittest для тестирования класса Calculator
    """

    def test_summ(self):
        """
        Тест на правильность выполнения функции сложения
        :return: Ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().summ('a', 5)
        self.assertEquals('Аргументы должны быть числами', error.exception.args[0])

    def test_difference(self):
        """
        Тест на правильность выполнения функции вычитания
        :return: ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().difference('a', 5)
        self.assertEquals('Аргументы должны быть числами', error.exception.args[0])

    def test_multiply(self):
        """
        Тест на правильность выполнения функции умножения
        :return: ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().multiply('a', 5)
        self.assertEquals('Аргументы должны быть числами', error.exception.args[0])

    def test_divide(self):
        """
        Тест на правильность выполнения функции деления
        :return: ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().divide('a', 5)
        self.assertEquals('Аргументы должны быть числами', error.exception.args[0])

    def test_exponentiation(self):
        """
        Тест на правильность выполнения функции возведения в степень
        :return: ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().exponentiation('a', 5)
        self.assertEquals('Аргументы должны быть числами', error.exception.args[0])

    def test_square_root(self):
        """
        Тест на правильность выполнения функции вычисления корня
        :return: ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().square_root('a', 5)
        self.assertEquals('Аргумент должны быть числом', error.exception.args[0])

    def test_percent(self):
        """
        Тест на правильность выполнения функции вычисления процента
        :return: ничего не возвращает
        """
        with self.assertRaises(ValueError) as error:
            Calculator().percent('a', 5)
        self.assertEquals('Аргументы должны быть числами', error.exception.args[0])
