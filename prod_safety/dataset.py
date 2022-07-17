import pandas as pd
from typing import Dict, List


def get_ids(df: pd.DataFrame) -> Dict[str, List[int]]:
    not_nan_ids = df[~df['Общее наименование продукции'].isna()].index.to_list()
    valid_tn_ved_ids = df.loc[~df['Общее наименование продукции'].isna() & (~df['Коды ТН ВЭД ЕАЭС'].isna())].index.to_list()
    return {'not_nan_ids': not_nan_ids, 'valid_tn_ved': valid_tn_ved_ids}