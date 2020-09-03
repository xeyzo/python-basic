def fix_odd_even_indices(source_array):
    odd_numbers = sorted([n for n in source_array if n%2!=0])
    c = 0
    res = []
    for i in source_array:
        if i %2!=0:
            res.append(odd_numbers[c])
            c += 1
        else:
            res.append(i)
    print(res)

numbers = [9,4,2,4,1,5,3,0]
fix_odd_even_indices(numbers)