import re

import pandas as pd


def filter_wos(data: object) -> object:
    data = data.filter([ "Article Title", "N"])
    data.rename(columns={"Article Title": "Title"}, inplace=True)
    data_list = data["Title"].to_list()
    result_list = []
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
    result_list = []
    for elem in data_list:
        if isinstance(elem, float):
            result_list.append("not")
            continue
        elem = elem.upper()
        elem = re.sub("[^A-Za-z0-9]", "", elem)
        result_list.append(elem)
    data["KEY"] = result_list
    return data


def count_total(data: object, flag: bool, iw1: float, iw2: float, total: float) -> float:
    n_list = data["N"].to_list()
    for i in n_list:
        if flag and float(i) < 1:
            total += float(i) * iw1
        else:
            total += float(i) * iw2
    return total


def main():
    iw1_1, iw1_2 = 138, 138
    iw2_1, iw2_2 = 51.1, 51.1
    iw3_1, iw3_2 = 18.9, 18.9
    iw4_1, iw4_2 = 7, 7
    iw_other_1, iw_other_2 = 7, 7

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

    total += count_total(w1_data, flag, iw1_1, iw1_2, total)
    total += count_total(w2_data, flag, iw2_1, iw2_2, total)
    total += count_total(w3_data, flag, iw3_1, iw3_2, total)
    total += count_total(w4_data, flag, iw4_1, iw4_2, total)
    total += count_total(w_none_data, flag, iw_other_1, iw_other_2, total)
    print(total)
    all_data = pd.concat(
        [s1_data, s2_data, s3_data, s4_data, s_none_data, w1_data, w2_data, w3_data, w4_data, w_none_data])
    all_data = all_data.drop_duplicates(keep=False)
    all_data["total"] = total
    all_data.to_excel("all_data.xlsx", index=False)
