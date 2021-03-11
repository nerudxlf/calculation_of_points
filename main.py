import math
import re

import pandas as pd


def filter_wos(data: object) -> object:
    data = data.filter(["Article Title", "N"])
    data.rename(columns={"Article Title": "Title", "N": "N_wos"}, inplace=True)
    data_list = data["Title"].to_list()
    result_list: list = []
    for elem in data_list:
        if isinstance(elem, float):
            result_list.append("not")
            continue
        elem = elem.upper()
        elem = re.sub("[^A-Za-z0-9]", "", elem)
        result_list.append(elem)
    data["KEY"] = result_list
    return data


def filter_scopus(data: object) -> object:
    data = data.filter(["Title", "N"])
    data_list = data["Title"].to_list()
    result_list: list = []
    for elem in data_list:
        if isinstance(elem, float):
            result_list.append("not")
            continue
        elem = elem.upper()
        elem = re.sub("[^A-Za-z0-9]", "", elem)
        result_list.append(elem)
    data["KEY"] = result_list
    return data


def count_total(data: object, flag: bool, iw1: float, total: float, n: str) -> float:
    n_list: list = data[n].to_list()
    for i in n_list:
        if math.isnan(float(i)):
            continue
        if flag and float(i) < 1:
            total += float(i) * iw1 * 1.2
        else:
            total += float(i) * iw1
    return total


def main():
    iw1_1: float = 138
    iw2_1: float = 51.1
    iw3_1: float = 18.9
    iw4_1: float = 7
    iw_other_1: float = 7
    n_wos: str = "N_wos"
    n: str = "N"
    flag: bool = False
    total: float = 0

    s1_data = filter_scopus(pd.read_excel("s1.xlsx"))
    s2_data = filter_scopus(pd.read_excel("s2.xlsx"))
    s3_data = filter_scopus(pd.read_excel("s3.xlsx"))
    s4_data = filter_scopus(pd.read_excel("s4.xlsx"))
    s_none_data = filter_scopus(pd.read_excel("s_none.xlsx"))
    w1_data = filter_wos(pd.read_excel("w1.xlsx"))
    w2_data = filter_wos(pd.read_excel("w2.xlsx"))
    w3_data = filter_wos(pd.read_excel("w3.xlsx"))
    w4_data = filter_wos(pd.read_excel("w4.xlsx"))
    w_none_data = filter_wos(pd.read_excel("w_none.xlsx"))

    total = count_total(w1_data, flag, iw1_1, total, n_wos)
    total = count_total(w2_data, flag, iw2_1, total, n_wos)
    total = count_total(w3_data, flag, iw3_1, total, n_wos)
    total = count_total(w4_data, flag, iw4_1, total, n_wos)
    total = count_total(w_none_data, flag, iw_other_1, total, n_wos)
    all_data = pd.concat(
        [s1_data, s2_data, s3_data, s4_data, s_none_data, w1_data, w2_data, w3_data, w4_data, w_none_data])
    df_data = all_data.filter(["KEY"])
    print(len(df_data.index))
    df_data = df_data.drop_duplicates(keep=False)
    print(len(df_data.index))
    result_data = pd.merge(left=df_data, right=all_data, left_on="KEY", right_on="KEY")
    print(len(result_data.index), len(all_data.index))
    total = count_total(result_data, flag, iw_other_1, total, n)
    print(total)
    result_data.to_excel("all_data.xlsx", index=False)
