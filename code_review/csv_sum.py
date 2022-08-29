import pandas as pd
from typing import Optional
from argparse import ArgumentParser

"""
1) Логика разделена на отдельные функции:
   get_parser() -- создает парсер аргументов (путь к файлу и контрольная сумма)
   read_data() -- читает csv файл,
   check() -- проверяет сумму;
2) Путь к файлу передается в read_data() в качестве аргумента, так скрипт может быть использован для чтения любого 
   .csv файла;
3) Метод read_data() обернут в конструкцию try/except - функция будет поднимать ошибку если указанный файл не найден, 
   или пуст;
4) С помощью select_dtypes в функцию check() передаются данные типа int и float, если в .csv файле будет колонка с 
   данными типа str - она отсеется (предполагается, что в колонках данные одного типа);
5) Внутри функции check() добавлен метод fillna(0), который  заменит осутствующие данные объектов (если такие будут
   в .csv файле) на числовые значения (в нашем случае на 0)
6) Для ускорения вычислений в check() массив конвертируется в numpy array с помощью метода to_numpy()

"""


def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, action='store', default='data.csv')
    parser.add_argument('--control_sum', type=int, action='store', default=10)
    return parser


def check(
        data: pd.DataFrame,
        control_sum: int = 10
) -> bool:
    """
    Проверяет соответствие суммы контрольному числу
    :param data: датафрейм с данными
    :param control_sum: контрольная сумма
    :return: флаг соответствия
    """
    return data.fillna(0).to_numpy().sum() == control_sum


def read_data(path: str = 'data.csv') -> Optional[pd.DataFrame]:
    """
    Считывает данные из файла
    :param path: путь к файлу
    :return: датафрейм со считанными данными
    """
    try:
        df = pd.read_csv(path, header=None)
        return df.select_dtypes(include=['float64', 'int64'])
    except pd.errors.EmptyDataError as error:
        raise error("No data in file")
    except FileNotFoundError as error:
        raise error


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    print(check(read_data(args.path), args.control_sum))
