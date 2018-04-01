import json

def json_line_load(file_name):
    with open(file_name, "r") as f:
        return json_line_loads(f.readlines())

def json_line_loads(contents):
    result = []
    for line in contents:
        result.append(json.loads(line))

    return result
