from datetime import datetime, timedelta
from random import randrange
from collections import deque
import csv
import os
import time
import pandas as pd
from sqlalchemy import create_engine, text


def is_empty_csv(FILE_PATH: str) -> bool:
    """
    Проверяет пустой ли файл логов перед ручным вводом
    """
    with open(f'{FILE_PATH}', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, _ in enumerate(reader):
            if i:
                return False
    return True


class CallingLogs:
    fist_time_record: datetime = datetime(1987, 1, 1, 0, 0, 0)  # Первый звонок для генерации
    last_time_record: datetime = fist_time_record  # От него со случайным шагом генерируется следующий звонок
    max_simult_calls: int = 0   # Записывает максимальное кол-во звонков на текущий момент

    def __init__(self, file_path: str = 'data/calling_logs.csv', engine=None, table_name: str = 'calling_logs'):
        self.FILE_PATH = file_path  # Путь к файлу для записи логов
        self.current_calls = deque()  # Записывает текущие звонки
        self.engine = engine  # Для подключения к базе данных
        self.table_name = table_name  # Название таблицы

    def generate_random_single_date(self) -> datetime:
        """
        Генерит время начала звонка со случайным шагом относительно предыдущего
        """
        max_time_between_calls = 15
        gen_datetime = self.last_time_record + timedelta(minutes=randrange(max_time_between_calls))
        self.last_time_record = gen_datetime
        return gen_datetime

    def put_in_curr_calls(self, call_start: datetime, duration: timedelta) -> None:
        """
        Добавляет в список текущих звонков новый
        """
        call_end = call_start + duration
        self.current_calls.append(call_end)
        self.current_calls = deque(sorted(self.current_calls))
        self.pop_ended_calls(call_start)
        self.max_simult_calls = max(self.max_simult_calls, len(self.current_calls))

    def pop_ended_calls(self, call_start: datetime) -> None:
        """
        Удаляет из списка текущих звонков те, которые уже закончились
        """
        older_call = self.current_calls.popleft()
        if older_call >= call_start:
            self.current_calls.appendleft(older_call)
        else:
            self.pop_ended_calls(call_start)

    def generated_filling(self, calls_count: int = 1050, max_call_duration: int = 60) -> None:
        """
        Пишет в новый (или очищает старый) файл случайные записи звонков
        в указанном количестве и в пределах заданной максимальной продолжительности
        """
        with open(f'{self.FILE_PATH}', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['call_start', 'duration', 'call_end'])
            for _ in range(calls_count):
                curr_call_start = self.generate_random_single_date()
                duration_td = timedelta(minutes=randrange(0, max_call_duration))
                writer.writerow([curr_call_start.strftime("%Y-%m-%d %H:%M:%S"), duration_td.seconds//60,
                                 (curr_call_start+duration_td).strftime("%Y-%m-%d %H:%M:%S")])
                self.put_in_curr_calls(curr_call_start, duration_td)

    def manual_add(self, call_start: datetime, duration: int) -> None:
        """
        Добавляет запись в файл ручным вводом, начало звонка - datetime, длительность - int в минутах
        """
        with open(f'{self.FILE_PATH}', 'a', newline='', encoding='utf-8') as file:
            file.seek(0, os.SEEK_END)
            writer = csv.writer(file)
            if is_empty_csv(self.FILE_PATH):
                writer.writerow(['call_start', 'duration', 'call_end'])
            duration_td = timedelta(minutes=duration)
            writer.writerow([call_start, duration,
                             (call_start+duration_td).strftime("%Y-%m-%d %H:%M:%S")])
            self.last_time_record = call_start
            self.put_in_curr_calls(call_start, duration_td)

    def display_content(self, req_count: int = 0) -> None:
        """
        Выводит на экран записи из логов, если req_count пуст - выводит все записи
        если req_count указан - выводит заданное количество записей с конца
        """
        with open(f'{self.FILE_PATH}', 'r', newline='', encoding='utf-8') as file:
            if req_count == 0:
                csvreader = csv.reader(file)
                for row in csvreader:
                    print(row)
            else:
                q = deque(file, req_count)
                q.reverse()
                print(*q)

    def get_max_simult_calls(self):
        """
        Возвращает значение максимального количество звонков
        """
        return self.max_simult_calls

    def clear_file_logs(self) -> None:
        """
        Очищает файл лога звонков
        """
        with open(f'{self.FILE_PATH}', 'w+'):
            pass

    def push_to_db(self) -> None:
        """
        Записывает данные из файла логов звонков в базу данных
        """
        with open(f'{self.FILE_PATH}', 'r') as file:
            file.seek(0)
            data = pd.read_csv(file, delimiter=',', parse_dates=['call_start', 'call_end'])
            data.to_sql(f'{self.table_name}', con=self.engine, if_exists='replace', chunksize=1000)

    def pull_from_db(self) -> None:
        """
        Считывает записи из базы данных
        """
        sql_query = pd.read_sql_query(sql=text(f'SELECT call_start, duration FROM {self.table_name}'),
                                      con=self.engine.connect())
        df = pd.DataFrame(sql_query)
        self.current_calls = []
        for i in range(len(df)):
            call_start = df.iloc[i]['call_start'].to_pydatetime()
            duration = timedelta(minutes=int(df.iloc[i]['duration']))
            self.put_in_curr_calls(call_start, duration)
            self.last_time_record = call_start


if __name__ == '__main__':
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5433/Testirovschiki")
    print('Создание записей')
    start_time = time.time()
    CL = CallingLogs(engine=engine)
    CL.generated_filling(1000)
    CL.display_content(10)
    print('Максимальное количество одновременных звонков: ', CL.get_max_simult_calls())
    elapsed_time = time.time() - start_time
    CL.push_to_db()
    print('Время выполнения программы: ', elapsed_time)
    CL.clear_file_logs()
    print('Считывание информации из базы данных')
    start_time = time.time()
    CL.pull_from_db()
    print('Максимальное количество одновременных звонков: ', CL.get_max_simult_calls())
    elapsed_time = time.time() - start_time
    print('Время выполнения программы: ', elapsed_time)
