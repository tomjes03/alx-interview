#!/usr/bin/python3
""" Module to calculate change. """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given amount total

    Arguments:
    coins: list of the values of your the coins
    total: given amount

    Returns:
    change: fewest number of coins needed to meet total
    """
    if total < 1:
        return 0

    # verify coins is a valid
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    my_coins = sorted(coins, reverse=True)
    money_left = total

    for coin in my_coins:
        while (money_left % coin >= 0 and money_left >= coin):
            change += money_left // coin
            money_left = money_left % coin

    change = change if money_left == 0 else -1

    return change
