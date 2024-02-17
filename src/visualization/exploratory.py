import matplotlib.pyplot as plt
import seaborn as sns

from src.data.raw_handler import get_raw_data_dict_csv


def show_boxplot(component_to_show: str):
    raw_dict = get_raw_data_dict_csv()
    data = list()
    positions = list()
    used_keys = list()
    for key in raw_dict:
        if component_to_show in raw_dict[key].columns:
            data.append(raw_dict[key][component_to_show])
            positions.append(len(data))
            used_keys.append(key)
    if data:
        plt.boxplot(data, positions=positions)
        plt.xticks(positions, used_keys, rotation=45)
        plt.ylabel(component_to_show)
        plt.title(f'Boxplots of {component_to_show}')
        plt.grid(True)
        plt.show()


def show_pair_grid(experiment_name: str):
    raw_dict = get_raw_data_dict_csv()
    pair_grid_plot = sns.PairGrid(raw_dict[experiment_name])
    pair_grid_plot.map(plt.scatter)
    plt.show()
