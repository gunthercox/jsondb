import codecs
import sys
import io


try:
    # Use the faster cjson library if it is available
    import cjson as json

    json_encode = json.encode
    json_decode = json.decode

except ImportError:
    import json

    json_encode = json.dumps
    json_decode = json.loads


def encode(value):
    value = json_encode(value, ensure_ascii=False)
    if sys.version < '3':
        return unicode(value)
    return value


def decode(value):
    return json_decode(value, encoding='utf-8')


if sys.version < '3':

    # Python 2 and 3 unicode string compatability
    def u(x):
        return codecs.unicode_escape_decode(x)[0]

    # Dictionary iteration compatibility
    def iteritems(dictionary):
        return dictionary.iteritems()
else:
    def u(x):
        return x

    # Dictionary iteration compatibility
    def iteritems(dictionary):
        return dictionary.items()


def open_file_for_reading(*args, **kwargs):
    if sys.version < '3':
        kwargs['mode'] = 'rb+'
    else:
        kwargs['encoding'] = 'utf-8'
        kwargs['mode'] = 'r+'

    return io.open(*args, **kwargs)


def open_file_for_writing(*args, **kwargs):
    if sys.version < '3':
        kwargs['mode'] = 'w+'
    else:
        kwargs['encoding'] = 'utf-8'
        kwargs['mode'] = 'w+'

    return io.open(*args, **kwargs)
