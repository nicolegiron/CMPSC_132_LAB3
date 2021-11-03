# LAB3
#Due Date: 02/27/2021, 11:59PM

"""
### Collaboration Statement:

"""

#REMINDER: All functions should NOT contain any for/while loops or global variables.
#          Use recursion, otherwise no credit will be given


def lineUp(aList1, aList2):
    '''
        >>> lineUp([5, 8.9, 'a'], [6, 5, 4, 21, -9, 's', 8.9, 45, 1, 1, 'a', 3])
        True
        >>> lineUp([5, 8.9, 'a'], [6, 5, 4, 21, -9, 'a', 8.9, 45, 1, 1, 3])
        False
        >>> lineUp([5, 8.9, 'a'], [6, 5, 4, 21, -9, 'a', 45, 1, 1, 3])
        False
        >>> lineUp([2, -6, 5, 3], [6, 1, 0, 2, -6, 4, 12, 5, 2, 3])
        True
    '''
    if len(aList1) == 0:
        return True
    elif len(aList1) > len(aList2):
        return False
    elif aList1[0] == aList2[0]:
        return lineUp(aList1[1:], aList2[1:])
    return lineUp(aList1, aList2[1:])


def removing(aList):
    """
    >>> removing([7, 4, 0])
    [7, 4, 0]
    >>> myList=[7, 4, -2, 1, 9]
    >>> removing(myList)   # Found(-2) Delete -2 and 1
    [7, 4, 9]
    >>> myList
    [7, 4, -2, 1, 9]
    >>> removing([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
    [9]
    >>> removing([-3, -4, 5, -4, 1])  # Found(-3) Delete -3, -4 and 5. Found(-4) Delete -4 and 1
    []
    """
    if len(aList) == 0:
        return aList
    elif aList[0] < 0:
        return removing(aList[-aList[0]:])
    return aList[:1] + removing(aList[1:])


def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    if n < 10:
        return n
    last = n % 10
    n = n // 10
    if n % 10 == last:
        return neighbor(n)
    return neighbor(n) * 10 + last
