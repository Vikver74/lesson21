from abstract import Storage


class Store(Storage):
    def __init__(self, capacity=100):
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
        if len(self._items) > 0:
            for item in self._items.items():
                total_busy_space += item[1]
            return self._capacity - total_busy_space
        else:
            return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)

    def check_remove(self, title, quantity):
        if self._items.get(title) and self._items[title] >= quantity:
            return True
        else:
            return False

    def check_add(self, quantity):
        if self.get_free_space() >= quantity:
            return True
        else:
            return False
