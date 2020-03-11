import hashlib


def get_hash(path):

    with open(path, encoding='utf8') as file:
        for string in file:
            hash_object = hashlib.md5(string.encode())
            hash_string = hash_object.hexdigest()
            yield hash_string

