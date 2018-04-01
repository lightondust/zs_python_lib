def trans_dict(dict_list, key):
    result = {}
    for item in dict_list:
        result[item[key]] = item
    return result

