#!/usr/bin/env python3
""" Caching system """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defining the BaseCache class """

    def __init__(self):
        """ Initialize the parent attributes """
        super().__init__()

    def put(self, key, item):
        """
        Assigns value to the self.cache_data dictionary from the
        Parent class using a key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value associated with a key in cache_data"""
        if key:
            return self.cache_data.get(key)
        return None
