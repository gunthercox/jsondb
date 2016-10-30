from .compat import decode, encode, open_file_for_reading, open_file_for_writing


def read_data(file_path):
    """
    Reads a file and returns a json encoded representation of the file.
    """

    if not is_valid(file_path):
        write_data(file_path, {})

    db = open_file_for_reading(file_path)
    content = db.read()

    obj = decode(content)

    db.close()

    return obj

def write_data(path, obj):
    """
    Writes to a file and returns the updated file content.
    """
    with open_file_for_writing(path) as db:
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
