from abstract import Storage


class Shop(Storage):
    def __init__(self, capacity=20):
        self._capacity = capacity
        self._items = {}

    @property
    def capacity(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    def add(self, title, quantity):
        if self._items.get(title):
            self._items[title] += quantity
        else:
            self._items[title] = quantity

    def remove(self, title, quantity):
        self._items[title] -= quantity

    def get_free_space(self):
        total_busy_space = 0
        for item in self._items.items():
            total_busy_space += item[1]
        return self.capacity - total_busy_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)

    def check_add(self,title, quantity):
        if ((self.get_unique_items_count() < 6 or title in self._items.keys())
                and self.get_free_space() >= quantity):
            return True
        else:
            return False

