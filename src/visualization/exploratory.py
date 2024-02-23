import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.data.raw_handler import get_raw_data_dict_csv, get_five_summary_statistic
from src.features.pca import get_pca_dict


def show_boxplots() -> None:
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


def show_pair_grids() -> None:
    raw_dict = get_raw_data_dict_csv()
    for key in raw_dict:
        pair_grid_plot = sns.PairGrid(raw_dict[key])
        pair_grid_plot.map(plt.scatter)
        pair_grid_plot.fig.suptitle(f'{key}')
        plt.show()


def show_correlation_matrices() -> None:
    raw_dict = get_raw_data_dict_csv()
    for key in raw_dict:
        corr = raw_dict[key].corr()

        f, ax = plt.subplots(figsize=(9, 6))
        sns.heatmap(corr, annot=True, linewidths=1.5, fmt='.2f', ax=ax)
        ax.set_title(f'{key}')
        plt.show()


def show_pca_plots() -> None:
    raw_dict = get_raw_data_dict_csv()
    pca_dict = get_pca_dict(raw_dict)
    for key, pca_value in pca_dict.items():
        pca_df = pca_value[0]
        pca_per_var = pca_value[1]
        plt.scatter(pca_df.PC1, pca_df.PC2)

        plt.title(f'{key}')
        plt.xlabel(f'PC1 - {pca_per_var[0]}%')
        plt.ylabel(f'PC2 - {pca_per_var[1]}%')

        for sample in pca_df.index:
            plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

        plt.show()


def _delete_consumption_columns(user_dict: dict[str: pd.DataFrame]) -> dict[str: pd.DataFrame]:
    """
    Удаляет колонки F_fuel, F_air, F_steam и строчку count
    """
    for key in user_dict.keys():
        if '_steam' in key:
            user_dict[key].drop(columns=['F_fuel', 'F_steam'], index=['count'], inplace=True)
        else:
            user_dict[key].drop(columns=['F_fuel', 'F_air'], index=['count'], inplace=True)
    return user_dict


def show_five_summary_heatmap() -> None:
    five_summary: dict = _delete_consumption_columns(get_five_summary_statistic(show=False))
    diesel_heatmap: pd.DataFrame = five_summary['diesel_air'] - five_summary['diesel_steam']
    heavy_oil_heatmap: pd.DataFrame = five_summary['heavy_oil_air'] - five_summary['heavy_oil_steam']
    kerosene_heatmap: pd.DataFrame = five_summary['kerosene_air'] - five_summary['kerosene_steam']

    heatmaps: dict = {
        'diesel_heatmap': diesel_heatmap, 'heavy_oil_heatmap': heavy_oil_heatmap, 'kerosene_heatmap': kerosene_heatmap
    }
    for key in heatmaps.keys():
        f, ax = plt.subplots(figsize=(9, 6))
        sns.heatmap(heatmaps[key], annot=True, linewidths=1.5, fmt='.2f', ax=ax)
        ax.set_title(f'{key} (air - steam)')
        plt.show()
