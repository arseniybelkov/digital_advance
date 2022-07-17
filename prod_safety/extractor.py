from typing import List
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer


def extract_regl(df: pd.DataFrame) -> List[str]:
    return sorted(set(df[~df['Технические регламенты'].isna()]['Технические регламенты'].apply(lambda t: t.split('; ') if ';' in t else [t]).sum()))

def extract_groups(df: pd.DataFrame) -> List[str]:
    groups = sorted(set(df[~df['Группа продукции'].isna()]['Группа продукции'].apply(lambda t: t.split('; ') if ';' in t else [t]).sum()))
    
def create_one_hot(key: str, df: pd.DataFrame, one_hot: MultiLabelBinarizer) -> np.ndarray:
    return one_hot.fit_transform(df[~df[key].isna()][key].apply(lambda t: t.split('; ') if ';' in t else [t]))