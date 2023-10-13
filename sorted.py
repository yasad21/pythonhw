def reverse_sort_dictionary(dictionary):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[0], reverse=True)
    result_list = [(name, data[0]) for name, data in sorted_items]

    return result_list
