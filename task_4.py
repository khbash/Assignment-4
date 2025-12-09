def merge_guest_list(*lists):
    result = []

    for list in lists:
        for el in list:
            if el not in result:
                result.append(el)

    result.sort()
    return result

