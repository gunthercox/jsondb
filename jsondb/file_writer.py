from . import json_coder


def read_data(path):
    """
    Reads a file and returns a json encoded representation of the file.
    """
    db = open(path, "r+")
    content = db.read()

    obj = json_coder.decode(content)

    db.close()

    return obj

def write_data(path, obj):
    """
    Writes to a file and returns the updated file content.
    """
    with open(path, "w+") as db:
        db.write(json_coder.encode(obj))

    return obj
