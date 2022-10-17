#!/usr/bin/env python3


def most_freq_int(arr):
    '''Finds the most frequent integer in an array.'''
    prev_count = 0
    most_freq_ans = 0

    i = 0
    while i < len(arr):
        # resets count after j loop exit
        count = 0

        # for each integer, loop through arr again
        # and see how many times it occurs using count
        j = 0
        while j < len(arr):

            # each time it occurs increment count
            if arr[i] == arr[j]:
                count += 1
            j += 1

        # after counting how many times it occured
        # compare with previous count
        # if it's greater then it's the most frequent answer
        if count > prev_count:
            prev_count = count
            most_freq_ans = arr[i]
        i += 1

    return most_freq_ans
