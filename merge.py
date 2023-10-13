def merged_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists.")

    if any(not isinstance(item, int) for item in list1) or any(not isinstance(item, int) for item in list2):
        raise TypeError("Lists must only contain integers.")
    merged_list = list1 + list2
    n = len(merged_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if merged_list[min_index] > merged_list[j]:
                min_index = j
        temp = merged_list[i]
        merged_list[i] = merged_list[min_index]
        merged_list[min_index] = temp
