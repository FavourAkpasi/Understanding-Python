def split_list(lst: list, num_sublists: int) -> list:
    final_list = []
    if num_sublists <= 0:
        final_list = lst
        return final_list
    else:
        final_list = [[] for _ in range(num_sublists)]
        for i, item in enumerate(lst):
            sublist_index = i % num_sublists
            final_list[sublist_index].append(item)

        return final_list


# split_list([0, 1, 2, 3, 4, 5, 6, 7], 4)
