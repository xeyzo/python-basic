def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

def find_missing_letter(chars):
    numbers = list(map(ord, chars))
    n = missing_elements(numbers)
    return chr(n[0])

chars = ["c","d","e","g","h"]
chars2 = ["X","Z"]
print('list_letters_first =', find_missing_letter(chars))
print('list_letters_second =', find_missing_letter(chars2))