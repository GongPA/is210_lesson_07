#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Get that fruit """

from data import FRUIT


def get_cost_per_item(shoplist):
    """
        Takes exactly one argument: a dictionary called shoplist.
        The key of shoplist should be the item name as found in FRUIT
        The value of shoplist should be an integer indicating the number
        of units to purchase.
        In one line, use a dictionary comprehension to:
        Iterate over the shoplist
        Filter results for shoplist to only return keys found in FRUIT
        Multiply the number of units from shoplist by the price of
        the units found in FRUIT.
        Return a new dictionary with the total cost per-item reflected.
    """
    fruit_cost = {key:value * FRUIT[key]
                  for key, value in shoplist.items()
                  if FRUIT.has_key(key)}
    return fruit_cost


def get_total_cost(shoplist):
    """
        Takes exactly one argument: a dictionary called shoplist.
        The key of shoplist should be the item name as found in FRUIT
        The value of shoplist should be an integer indicating the
        number of units to purchase.
        In a single-line:
        Uses get_cost_per_item() to retrieve the per-item costs.
        Sums the values of the resultant dictionary together.
        Tip
        Check out the sum() function to help with this. There's also a
        helpful dictionary built-in function you might want to use.
        Returns the total cost.
    """
    return sum(get_cost_per_item(shoplist).values())
