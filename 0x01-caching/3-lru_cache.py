#!/usr/bin/env python3
""" LRU Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defining the LIFO Caching Model """
    __LRU = []

    def __init__(self):
        """ Initializing the Parent Class """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache using a key """
        if key and item:
            if key in self.cache_data.keys():
                if key in self.__LRU:
                    index = self.__LRU.index(key)
                    self.
                self.__LRU.add(key)
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                least_used_key = list(iter(self.__LRU))[0]
                self.__LRU.discard(least_used_key)
                del self.cache_data[least_used_key]
                print(f'DISCARD: {least_used_key}')
                self.__LRU.add(key)
                self.cache_data[key] = item
            else:
                self.__LRU.discard(key)
                self.__LRU.add(key)
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with a key in a cache """
        if key:
            if key in self.cache_data.items():
                self.__LRU.discard(key)
                self.__LRU.add(key)
            return self.cache_data.get(key)

        return None
