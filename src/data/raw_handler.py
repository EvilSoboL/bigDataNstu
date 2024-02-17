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


def get_five_summary_statistic():
    raw_dict = get_raw_data_dict_csv()
    for key, value in raw_dict.items():
        print(key)
        display(value.describe())
