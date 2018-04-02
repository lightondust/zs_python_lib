"""
辞書を変換するための関数たち
"""

def list_to_dict(dict_list, key):
    """
    辞書のリストを受け取って特定のkeyの各辞書の値をkeyにして新しい辞書を作る。
    """
    result = {}
    for item in dict_list:
        result[item[key]] = item
    return result

