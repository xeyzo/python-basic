numbers = [9,4,2,4,1,5,3,0]


odd_numbers = [n for n in numbers if n%2!=0]
odd_numbers = sorted(odd_numbers)

print(odd_numbers)