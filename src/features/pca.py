import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing


def get_pca_dict(raw_dict:  dict[str: pd.DataFrame]) -> dict[str: pd.DataFrame]:
    pca_dict = dict()
    for key, value in raw_dict.items():
        scaled_data = preprocessing.scale(value.T)
        pca = PCA()
        pca.fit(scaled_data)
        pca_data = pca.transform(scaled_data)

        per_var = np.round(pca.explained_variance_ratio_*100, decimals=1)
        labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
        pca_df = pd.DataFrame(pca_data, index=value.columns, columns=labels)
        pca_dict[key] = pca_df
    return pca_dict
