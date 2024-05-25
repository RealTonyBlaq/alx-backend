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
            
