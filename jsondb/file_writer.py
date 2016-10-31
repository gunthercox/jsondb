from .compat import decode, encode


def read_data(file_path):
    """
    Reads a file and returns a json encoded representation of the file.
    """

    if not is_valid(file_path):
        write_data(file_path, {})

    db = open(file_path, 'r+', encoding='utf-8')
    content = db.read()

    obj = decode(content)

    db.close()

    return obj

def write_data(path, obj):
    """
    Writes to a file and returns the updated file content.
    """
    with open(path, 'w+', encoding='utf-8') as db:
        db.write(encode(obj))

    return obj

def is_valid(file_path):
    """
    Check to see if a file exists or is empty.
    """
    from os import path, stat

    can_open = False

    try:
        with open(file_path) as fp:
            can_open = True
    except IOError:
        return False

    is_file = path.isfile(file_path)

    return path.exists(file_path) and is_file and stat(file_path).st_size > 0
