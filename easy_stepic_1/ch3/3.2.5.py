# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    if d.get(key) != None:
        d[key] += [value]
    elif d.get(2 * key) != None:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
