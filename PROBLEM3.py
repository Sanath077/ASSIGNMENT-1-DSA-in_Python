def rotatelist(l, k):
    if k <= 0:
        return l
    k = k % len(l)
    return l[k:] + l[:k]
# This is a Python function "rotatelist" that takes in two parameters: a list "l" and an integer "k".
###################################################################################################################################
# The function performs a left rotation on the list by "k" elements.
# If "k" is less than or equal to 0, it returns the original list without any rotation.
# Otherwise, it calculates the modulo of "k" and the length of the list,
# which gives the actual number of rotations to be performed in case "k" is greater than the length of the list.
# Finally, it returns the concatenation of two sub-lists: the elements from the "k"th position to the end of the list,
# and the elements from the start of the list to the "k-1"th position.
