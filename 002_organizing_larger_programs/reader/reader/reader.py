import os

from reader.compressed import gzipped, bzipped
# from .compressed import gzipped, bzipped # With relative imports

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, mode='rt')

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()
