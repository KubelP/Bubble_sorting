'Sorting of numbers in list using bubble method'

def bubble_sorting(list_numbers_to_sort):
    '''Bombel sortinf function give unsorted list returned sorted list'''
    
    for _ in range(len(list_numbers_to_sort)):
        for index in range(len(list_numbers_to_sort)-1):
            if list_numbers_to_sort[index] > list_numbers_to_sort[index+1]:
                list_numbers_to_sort[index], list_numbers_to_sort[index+1] = \
                    list_numbers_to_sort[index+1], list_numbers_to_sort[index]
    return list_numbers_to_sort
