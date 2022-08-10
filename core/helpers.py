import os
import pathlib
from io import StringIO


BASE_PATH = pathlib.Path(os.getcwd()).parent.absolute()
DATA_DIR = os.path.join(BASE_PATH, 'include')


def get_frequencies(filename):
    result = dict()
    with open(os.path.join(DATA_DIR, filename), 'r') as fin:
        data = fin.read().split('\n')

    for i in data:
        i = i.rsplit()
        if len(i) > 0:
            result[i[0]] = i[2]
    return result


def get_encoded(filename):
    results = list()

    with open(os.path.join(DATA_DIR, filename), 'r') as fin:
        data = fin.read().split('\n')

    for i in data:
        if i != '':
            results.append(i)

    return results


class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def add(self, string):
        self._file_str.write(string)

    def __str__(self):
        return self._file_str.getvalue()
