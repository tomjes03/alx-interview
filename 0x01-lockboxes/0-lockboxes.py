#!/usr/bin/python3
"""  a method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened

    Arguement:
        boxes: list of lists

    """
    keys_set = {0}
    keys_set.update(boxes[0])
    keys_in_hand = [] + boxes[0]

    for key in keys_in_hand:
        if key < len(boxes) and key >= 0:
            keys_set.update(boxes[key])
        new_keys = keys_set - set(keys_in_hand)
        keys_in_hand += new_keys

    useful_keys = [k for k in keys_set if k < len(boxes)]
    if len(useful_keys) == len(boxes):
        return True
    return False
