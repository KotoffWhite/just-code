import unittest
from db_callinglogs import CallingLogs
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import csv


class TestCallingLogs(unittest.TestCase):
    """Проверка работы модуля учёта звонков"""

    @classmethod
    def is_empty_csv(cls, FILE_PATH: str) -> bool:
        """
        Проверяет пустой ли файл логов перед ручным вводом
        """
        with open(f'{FILE_PATH}', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for i, _ in enumerate(reader):
                if i:
                    return False
        return True

    @classmethod
    def setUpClass(cls):
        cls.test_file = 'data/test_data.csv'
        first_date = datetime(2020, 1, 1, 15, 0, 0)
        cls.set_up_table = []
        cls.result_table = [['call_start', 'duration', 'call_end'], ]
        for i in range(60):
            cls.set_up_table.append([first_date+timedelta(minutes=i), 12])
            cls.result_table.append([str(first_date+timedelta(minutes=i)), '12',
                                     str(first_date+timedelta(minutes=(i+12)))])
        cls.result_table.append([])

    def tearDown(self):
        with open(f'{self.test_file}', 'w+'):
            pass

    def setUp(self):
        self.CL = CallingLogs(file_path=self.test_file, table_name='callings_test')

    def test_manual_add_to_csv_file(self):
        """Проверяем, что записи в csv файл заносятся верно"""
        for row in self.set_up_table:
            self.CL.manual_add(row[0], row[1])
        with open(f'{self.test_file}', 'r', newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                self.assertEqual(row, self.result_table[i])
                i += 1

    def test_get_max_simult_calls(self):
        """Проверяем верность максимального числа одновременных звонков"""
        for row in self.set_up_table:
            self.CL.manual_add(row[0], row[1])
        self.assertEqual(self.CL.get_max_simult_calls(), 13)

    def test_clear_file_logs(self):
        """Проверяем очистку файла csv для логов"""
        for row in self.set_up_table:
            self.CL.manual_add(row[0], row[1])
        self.CL.clear_file_logs()
        self.assertTrue(self.is_empty_csv(self.test_file))

    def test_get_max_from_db(self):
        """Проверяем верность макс числа звонков через базу данных"""
        self.CL.engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5433/Testirovschiki")
        for row in self.set_up_table:
            self.CL.manual_add(row[0], row[1])
        self.CL.push_to_db()
        self.CL.pull_from_db()
        self.assertEqual(self.CL.get_max_simult_calls(), 13)


if __name__ == "__main__":
    unittest.main()
