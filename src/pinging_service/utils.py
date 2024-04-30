import json


def byte_string_to_dict(byte_string):
    return json.loads(byte_string.decode("utf-8"))
