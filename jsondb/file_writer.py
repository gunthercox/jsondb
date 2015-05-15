from .util import decode, encode


def read_data(path):
    """
    Reads a file and returns a json encoded representation of the file.
    """
    db = open(path, "r+")
    content = db.read()

    obj = decode(content)

    db.close()

    return obj

def write_data(path, obj):
    """
    Writes to a file and returns the updated file content.
    """
    with open(path, "w+") as db:
        db.write(encode(obj))

    return obj

def is_valid(file_path):
    """
    Check to see if a file exists or is empty
    """
    from os import path, stat

    return not path.exists(file_path) or stat(file_path).st_size == 0
