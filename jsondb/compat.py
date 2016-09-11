import sys

'''
Use the faster cjson library if it is available
'''

try:
    import cjson as json

    json_encode = json.encode
    json_decode = json.decode

except ImportError:
    import json

    json_encode = json.dumps
    json_decode = json.loads


def encode(value):
    return json_encode(value)


def decode(value):
    return json_decode(value)


if sys.version < '3':

    # Python 2 and 3 unicode string compatability
    import codecs
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
