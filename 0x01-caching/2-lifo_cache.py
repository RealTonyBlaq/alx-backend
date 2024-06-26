#!/usr/bin/env python3
""" LIFO Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defining the LIFO Caching Model """

    def __init__(self):
        """ Initializing the Parent Class """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache using a key """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lifo_key = list(iter(self.cache_data.keys()))[-1]
                del self.cache_data[lifo_key]
                print(f'DISCARD: {lifo_key}')
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with a key in a cache """
        if key:
            return self.cache_data.get(key)

        return None
