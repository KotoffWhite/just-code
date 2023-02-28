import unittest

from two_sum_extra_ds import two_sum_extra_ds
from A_function_result import parabolic_equ
from B_even_and_uneven import same_evennes
from D_chaotic_weather import count_chaotic_days
from E_the_longest_word import get_the_longest_word
from F_Palindrom import check_palindrom
from G_work_homeoffice import decimal_to_binary
from H_binary_summ import binary_sum
from I_power_of_four import check_if_power_of_four
from J_factorization import factorize
from K_list_form_for_numbers import get_sum
from M_A_nearest_zero import get_zero_distance


class TestTwoSumExtraDs(unittest.TestCase):
    """Тестируем two_sum при использовании дополнительной структуры данных"""

    @classmethod
    def setUpClass(cls):
        cls.set_up_dict = {
            ('-9 -7 -6 -1 -1 3', 2): '-1 3',
            ('-9 -7 -6 -1 -1 3 5 15', 100): None,
        }

    def test_two_sum_extra_ds(self):
        for in_data in self.set_up_dict.keys():
            numb_list = list(map(int, in_data[0].split()))
            x = in_data[1]
            self.assertEqual(two_sum_extra_ds(numb_list, x), self.set_up_dict[in_data])


class TestParabolicEqu(unittest.TestCase):
    """Тестируем parabolic_equ"""

    @classmethod
    def setUpClass(cls):
        cls.set_up_dict = {
            '-8 -5 -2 7': -183,
            '8 2 9 -10': 40,
        }

    def test_parabolic_equ(self):
        for in_data in self.set_up_dict.keys():
            a, x, b, c = map(int, in_data.split())
            self.assertEqual(parabolic_equ(a, x, b, c), self.set_up_dict[in_data])


class TestEvenUneven(unittest.TestCase):
    """Тестируем проверку одинаковой четности чисел"""

    @classmethod
    def setUpClass(cls):
        cls.input_str_list = ['1 2 -3', '7 11 7', '6 -2 0', ]
        cls.result_list = ['FAIL', 'WIN', 'WIN']

    def test_even_uneven_first(self):
        for i in range(len(self.input_str_list)):
            numbers = list(map(int, self.input_str_list[i].split()))
            self.assertEqual(same_evennes(numbers), self.result_list[i])


class TestChaoticWeather(unittest.TestCase):
    """Тестирует функцию поиска количества хаотичных дней"""

    @classmethod
    def setUpClass(cls):
        cls.temp_str_list = ['-1 -10 -8 0 2 0 5', '1 2 5 4 8', '-133']
        cls.result_list = [3, 2, 1]

    def test_chaotic_weather(self):
        for i in range(len(self.temp_str_list)):
            temp_list = list(map(int, self.temp_str_list[i].split()))
            self.assertEqual(count_chaotic_days(temp_list), self.result_list[i])


class TestLongestWord(unittest.TestCase):
    """Тестирует функцию поиска самого длинного слова"""

    @classmethod
    def setUpClass(cls):
        cls.temp_str_list = ['i love segment tree', 'frog jumps from river']
        cls.result_list = [('segment', 7), ('jumps', 5)]

    def test_longest_word(self):
        for i in range(len(self.temp_str_list)):
            self.assertEqual(get_the_longest_word(self.temp_str_list[i]), self.result_list[i])


class TestPalindrom(unittest.TestCase):
    """Тестирует функцию палиндрома"""

    @classmethod
    def setUpClass(cls):
        cls.temp_str_list = ['A man, a plan, a canal: Panama', 'zo']
        cls.result_list = [True, False]

    def test_palindrom(self):
        for i in range(len(self.result_list)):
            self.assertEqual(check_palindrom(self.temp_str_list[i]), self.result_list[i])


class TestDecimalToBinary(unittest.TestCase):
    """Тестирует функцию перевода в двоичную систему"""

    @classmethod
    def setUpClass(cls):
        cls.input_list = [5, 14, 0]
        cls.result_list = ['101', '1110', '0']

    def test_decimal_to_binary(self):
        for i in range(len(self.input_list)):
            self.assertEqual(decimal_to_binary(self.input_list[i]), self.result_list[i])


class TestBinarySumm(unittest.TestCase):
    """Тестирует бинарное сложение"""

    @classmethod
    def setUpClass(cls):
        cls.input_list = [('1', '1'), ('1010', '1011')]
        cls.result_list = ['10', '10101']

    def test_binary_sum(self):
        for i in range(len(self.input_list)):
            numb1 = self.input_list[i][0]
            numb2 = self.input_list[i][1]
            self.assertEqual(binary_sum(numb1, numb2), self.result_list[i])


class TestPowerOfFour(unittest.TestCase):
    """Тестирует является ли число степенью четвёрки"""

    @classmethod
    def setUpClass(cls):
        cls.input_list = [15, 16, 1, 0]
        cls.result_list = [False, True, True, False]

    def test_power_of_four(self):
        for i in range(len(self.input_list)):
            self.assertEqual(check_if_power_of_four(self.input_list[i]), self.result_list[i])


class TestFactorize(unittest.TestCase):
    """Тестирует возврат факторизации числа"""

    @classmethod
    def setUpClass(cls):
        cls.set_up_dict = {
            8: [2, 2, 2],
            13: [13],
            100: [2, 2, 5, 5],
            917521579: [13, 70578583],
        }

    def test_factorize(self):
        for in_data in self.set_up_dict.keys():
            self.assertEqual(factorize(in_data), self.set_up_dict[in_data])


class TestListForm(unittest.TestCase):
    """Тестирует сложение списочной формы и числа"""

    @classmethod
    def setUpClass(cls):
        cls.set_up_dict = {
            ('1 2 0 0', 34): ['1', '2', '3', '4'],
            ('9 5', 17): ['1', '1', '2'],
        }

    def test_list_form_summ(self):
        for in_data in self.set_up_dict.keys():
            input_list = in_data[0].split()
            self.assertEqual(get_sum(input_list, in_data[1]), self.set_up_dict[in_data])


class TestNearestZero(unittest.TestCase):
    """Тестирует нахождение расстояния до ближайшего нуля"""

    @classmethod
    def setUpClass(cls):
        cls.set_up_dict = {
            '0 1 4 9 0': [0, 1, 2, 1, 0],
            '0 7 9 4 8 20': [0, 1, 2, 3, 4, 5],
        }

    def test_nearest_zero(self):
        for data_in in self.set_up_dict.keys():
            self.assertEqual(get_zero_distance(data_in), self.set_up_dict[data_in])


if __name__ == "__main__":
    unittest.main()
