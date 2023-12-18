# Итератор для удаления дубликатов

class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = items
        self.ignore_case = kwargs.get("ignore_case", False)
        self.seen = set()

    def __next__(self):
        while True:
            value = next(self.data)
            if isinstance(value, str) and self.ignore_case:
                key = value.lower()
            else:
                key = value
            if key not in self.seen:
                self.seen.add(key)
                return value

    def __iter__(self):
        return self

    def lists(self):
        array = []
        for x in self:
            array.append(x)
        return array



data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
#data = [1, 2, 2, 3, 4, 4, 5]

if __name__ == '__main__':
    unique_items = Unique(iter(data))
    for item in unique_items:
        print(item)