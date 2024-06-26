#!/usr/bin/env python3
""" FIFO Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Defining the FIFO Caching Model """

    def __init__(self):
        """ Initializing the Parent Class """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache using a key """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                fifo_key = next(iter(self.cache_data))
                del self.cache_data[fifo_key]
                print(f'DISCARD: {fifo_key}')
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with a key in a cache """
        if key:
            return self.cache_data.get(key)

        return None
