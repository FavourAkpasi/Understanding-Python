def sort(elements: list, ascending: bool = True):
    e=elements
    for i in range(1, len(elements)):
        j = i
        while j > 0 and elements[j - 1] > elements[j]:
            elements[j], elements[j - 1] = elements[j - 1], elements[j]
            j -= 1
    if not ascending:
        elements.reverse()
