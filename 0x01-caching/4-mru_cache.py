#!/usr/bin/env python3
""" MRU Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defining the MRU Caching Model """

    def __init__(self):
        """ Initializing the Parent Class """
        super().__init__()
        self.__MRU = []

    def put(self, key, item):
        """ Adds an item to the cache using a key """
        if key and item:
            if key in self.cache_data.keys():
                self.__MRU.remove(key)
                self.__LRU.append(key)
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                least_used_key = self.__LRU.pop(0)
                del self.cache_data[least_used_key]
                print(f'DISCARD: {least_used_key}')
                self.__LRU.append(key)
                self.cache_data[key] = item
            else:
                self.__LRU.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with a key in a cache """
        if key:
            if key in self.cache_data:
                self.__LRU.remove(key)
                self.__LRU.append(key)
            return self.cache_data.get(key)

        return None
