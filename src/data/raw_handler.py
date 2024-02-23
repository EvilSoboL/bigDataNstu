import os
import pandas as pd
from IPython.display import display

PROJECT_FOLDER = os.path.dirname('C:/Users/Mark/PycharmProjects/bigDataNstu/')
RAW_DATA = os.path.join(PROJECT_FOLDER, 'data', 'raw')


def get_raw_data_dict_csv() -> dict[str: pd.DataFrame]:
    raw_dict = dict()
    files = os.listdir(RAW_DATA)
    for file in files:
        path_to_file = os.path.join(RAW_DATA, file)
        df = pd.read_csv(path_to_file)
        raw_dict[file[:-4]] = df
    return raw_dict


def get_data_info_from_dict():
    raw_dict = get_raw_data_dict_csv()
    for key, value in raw_dict.items():
        print(key)
        value.info()


def get_five_summary_statistic(show: bool) -> dict[str: pd.DataFrame] | None:
    raw_dict: dict = get_raw_data_dict_csv()
    five_summary_dict: dict = dict()
    for key, value in raw_dict.items():
        if show:
            display(key)
            display(value.describe())
        else:
            five_summary_dict[key] = value.describe()
    if show:
        return None
    else:
        return five_summary_dict


def show_raw_data():
    raw_dict = get_raw_data_dict_csv()
    for key, value in raw_dict.items():
        display(key)
        display(value.head())


def delete_unused_columns_from_dict(raw_dict: dict[str: pd.DataFrame]) -> dict[str: pd.DataFrame]:
    for key, values in raw_dict.items():
        if 'F_air' in values.columns:
            columns_to_drop = ['F_fuel', 'F_air']
            values.drop(columns=columns_to_drop, inplace=True)
        else:
            columns_to_drop = ['F_fuel', 'F_steam']
            values.drop(columns=columns_to_drop, inplace=True)
    return raw_dict
