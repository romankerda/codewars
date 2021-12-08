def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    output = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i-1]:
            output.append(iterable[i])
    return output



print(unique_in_order(''))

