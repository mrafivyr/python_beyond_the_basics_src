store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        print(s)
        return s[-1]
    store.append(last_letter)
    return sorted(strings, key=last_letter)