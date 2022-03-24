from bubble_soriting import bubble_sorting

def test_sort_of_numbers():
    tested_unsorted_numbers = [29, 9, 53, 12, 88, 28, 22, 15, 1, 81]
    tested_sorted_numbers = bubble_sorting(tested_unsorted_numbers)
    for i in range(len(tested_sorted_numbers)-1):
        assert tested_sorted_numbers[i] < tested_sorted_numbers[i+1]
