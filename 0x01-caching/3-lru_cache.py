#!/usr/bin/env python3
""" LRU Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defining the LIFO Caching Model """
    __LRU = set()

    def __init__(self):
        """ Initializing the Parent Class """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache using a key """
        if key and item:
            if key in self.cache_data.keys():
                self.__LRU.discard(key)
                self.__LRU.add(key)
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                
                print(f'DISCARD: {lifo_key}')
                self.cache_data[key] = item
            else:
                3-lru_cache.py
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with a key in a cache """
        if key:
            if key in self.cache_data.items():
                self.__LRU.discard(key)
                self.__LRU.add(key)
            return self.cache_data.get(key)

        return None
