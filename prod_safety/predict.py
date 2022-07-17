import pandas as pd
from typing import List, Dict


def predict_regl(df: pd.DataFrame, regl: List[str], counts: List[int]) -> pd.DataFrame:
    def regl_prod(df, regl, counts):
        res = dict()
        for i in range(len(regl)):
            x = df[df[regl[i]] == 1]['parsed_prod'].to_list()
            cap_words = [word for word in (' '.join(x)).split()]
            word_counts = Counter(cap_words)
            res[regl[i]] = [j[0] for j in word_counts.most_common(counts[i])]
        return res

    r_prod = regl_prod(df, regl, counts)

    def check_regl(df, r_prod, regl):
        res_arr = []
        for i in not_nan_ids:
            tmp = set(df['parsed_prod'][i].split())
            res = dict()
            for r in regl:
                tmp1 = set(r_prod[r])
                res[r] = len(tmp.intersection(tmp1))
            sorted_tuple = sorted(res.items(), key=lambda x: x[1], reverse=True)
            res_arr.append(sorted_tuple[0][0])
        return res_arr

    t = check_regl(df, r_prod, regl)
    return pd.DataFrame(t, index=not_nan_ids, columns=['new_regl'])


def predict_group(df: pd.DataFrame) -> list:
    pass


def predict_tn_ved(df: pd.DataFrame, ids_list: List[int], TN_VED_TAGS: Dict[str, List[str]]) -> List[str]:
    predicted_tn_ved = []
    for idx in ids_list:
        points = {k: 0 for k, v in TN_VED_TAGS.keys()}
        for k, v in TN_VED_TAGS.items():
            points[k] = len(set(v).intersection(set(df.loc[idx, 'parsed_prods'].split(' '))))
        predicted_tn_ved.append(sorted(points.items(), key=lambda x: x[1], reverse=True)[0][0])
    return predicted_tn_ved