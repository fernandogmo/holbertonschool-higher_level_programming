#!/usr/bin/python3
''' Technical interview preparation: find peak in lowest time complexity'''


def find_peak(list_of_integers):
    ''' Finds a peak in a list of unsorted integers. '''
    l = list_of_integers
    return max(l) if l else None


if __name__ == '__main__':
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
