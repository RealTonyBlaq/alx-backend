#!/usr/bin/env python3
""" LFU Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


def get_lfu_key(lfu_dict):
    """ Returns the key with the lowest use count """
    sorted_ = sorted(lfu_dict.items(), key=lambda y: y[1])
    return sorted_[0][0]


class LFUCache(BaseCaching):
    """ Defining the LFU Caching Model. """

    def __init__(self):
        """ Initializing the Parent Class """
        super().__init__()
        self.__LFU = {}

    def put(self, key, item):
        """ Adds an item to the cache using a key """
        if key and item:
            if key in self.cache_data.keys():
                self.__LFU[key] += 1
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = get_lfu_key(self.__LFU)
                del self.cache_data[lfu_key]
                del self.__LFU[lfu_key]
                print(f'DISCARD: {lfu_key}')
                self.__LFU[key] = 1
                self.cache_data[key] = item
            else:
                self.__LFU[key] = 1
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with a key in a cache """
        if key:
            if key in self.cache_data:
                self.__LFU[key] += 1
            return self.cache_data.get(key)

        return None
