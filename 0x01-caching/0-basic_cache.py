#!/usr/bin/env python3
""" Caching system """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defining the BaseCache class """

    def __init__():
        """ Initial"""

    def put(self, key, item):
        """
        Assigns value to the self.cache dictionary from the
        Parent class using a key
        """
        if key and item:
            
