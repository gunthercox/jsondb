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
