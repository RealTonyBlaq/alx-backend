#!/usr/bin/env python3
""" FIFO Caching Model """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Defining the FIFO Caching Model """

    def __init__(self):
        """ Ini"""
