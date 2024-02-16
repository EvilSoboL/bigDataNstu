import matplotlib.pyplot as plt

from src.data.raw_handler import get_raw_data_dict_csv


class BoxPlot:
    def __init__(self):
        self.name = None

    def show_boxplots(self, component_to_show):
        raw_dict = get_raw_data_dict_csv()
        data = [raw_dict[key][component_to_show] for key in raw_dict]
        positions = range(1, len(raw_dict) + 1)

        plt.boxplot(data, positions=positions)
        plt.xticks(positions, raw_dict.keys(), rotation=45)
        plt.ylabel(component_to_show)
        plt.title(f'Boxplots of {component_to_show}')
        plt.grid(True)
        plt.show()
