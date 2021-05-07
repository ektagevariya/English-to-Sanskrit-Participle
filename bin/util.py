import collections
import csv


def key_fn(x):
    sounds = 'aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlLvSzsh|'
    assert all (L in sounds for L in x), x
    return tuple(sounds.index(L) for L in x)


class read_csv(object):

    def __init__(self, filename, labels=None):
        self.filename = filename
        self.labels = labels

    def __enter__(self):
        self.f = open(self.filename, 'r')
        self.reader = csv.DictReader(self.f, self.labels)
        return self.reader

    def __exit__(self, type, value, traceback):
        self.f.close()


def read_csv_rows(filename):
    with read_csv(filename) as reader:
        for row in reader:
            yield row


class write_csv(object):

    def __init__(self, filename, labels):
        self.filename = filename
        self.labels = labels

    def __enter__(self):
        self.f = open(self.filename, 'w')
        self.writer = csv.DictWriter(self.f, self.labels)
        self.writer.writeheader()
        return self.writer.writerow

    def __exit__(self, type, value, traceback):
        self.f.close()


def make_csv_string(labels, rows):
    """Print the given data as a CSV.

    :param labels: a list of labels
    :param rows: a list of lists of strings. Each inner list must have
                 a 1:1 correspondence with `labels`.
    """
    data = [','.join(labels)]
    data.extend(','.join([x or '' for x in row]) for row in rows)
    return '\n'.join(data)


def unique(items, key_fn=None):
    """Keep only the unique items in `items`, maintaining order.

    :param items: the list
    :param key_fn: a function that, given an item, returns some ID for
                   the item.
    """
    seen = set()
    returned = []
    for item in items:
        key = key_fn(item) if key_fn else item
        if key in seen:
            continue
        else:
            returned.append(item)
            seen.add(key)
    return returned

