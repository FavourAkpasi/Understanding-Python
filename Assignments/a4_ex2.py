def clip(*values, min_=0, max_=1) -> list:
    returned_list = []
    if len(values) == 0:
        return returned_list
    else:
        for value in values:
            if value < min_:
                returned_list.append(min_)
            elif value > max_:
                returned_list.append(max_)
            else:
                returned_list.append(value)
        return returned_list


# print(clip(1, 2, 0.1, 0))
