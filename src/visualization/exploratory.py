import matplotlib.pyplot as plt
import seaborn as sns

from src.data.raw_handler import get_raw_data_dict_csv


def show_boxplots():
    components = ['O2', 'CO', 'NO', 'NO2', 'NOx', 'CO2', 'SO2']
    for component_to_show in components:
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


def show_pair_grids():
    raw_dict = get_raw_data_dict_csv()
    for key in raw_dict:
        pair_grid_plot = sns.PairGrid(raw_dict[key])
        pair_grid_plot.map(plt.scatter)
        pair_grid_plot.fig.suptitle(f'{key}')
        plt.show()


def show_correlation_matrices():
    raw_dict = get_raw_data_dict_csv()
    for key in raw_dict:
        corr = raw_dict[key].corr()

        f, ax = plt.subplots(figsize=(9, 6))
        sns.heatmap(corr, annot=True, linewidths=1.5, fmt='.2f', ax=ax)
        ax.set_title(f'{key}')
        plt.show()
