#!/usr/bin/env python3
""" Caching system """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Definind the BaseCache class """

    def put(self, key, item):
        """
        Assigns value to the self.cache dictionary from the Parent class using a key
        """
