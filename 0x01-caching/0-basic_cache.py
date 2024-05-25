#!/usr/bin/env python3
""" Caching system """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defining the BaseCache class """

    def __init__():
        """ Initialize the parent attributes """
        super()

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
            