import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing


def get_pca_dict(raw_dict:  dict[str: pd.DataFrame]) -> dict[str: pd.DataFrame, list]:
    pca_dict = dict()
    for key, df in raw_dict.items():
        df = remove_consumption_columns(df)
        scaled_data = preprocessing.scale(df.T)
        pca = PCA()
        pca.fit(scaled_data)
        pca_data = pca.transform(scaled_data)

        per_var = np.round(pca.explained_variance_ratio_*100, decimals=1)
        labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
        pca_df = pd.DataFrame(pca_data, index=df.columns, columns=labels)
        pca_dict[key] = pca_df, per_var
    return pca_dict


def remove_consumption_columns(df: pd.DataFrame) -> pd.DataFrame:
    if 'F_air' in df.columns:
        df: pd.DataFrame = df.drop(['F_fuel', 'F_air'], axis=1)
    else:
        df: pd.DataFrame = df.drop(['F_fuel', 'F_steam'], axis=1)
    return df

