def find_max(list):
    maxcimum = list[0]
    for number in list:
        if number > maxcimum:
            maxcimum = number
    return maxcimum