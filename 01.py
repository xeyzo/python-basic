first = ['Behind', 'every', 'great', 'man']
second = ['is', 'a', 'woman']
third = ['rolling', 'her', 'eyes']

combine = first + second + third
listToStr = ' '.join([str(toStr) for toStr in combine]) 
print(listToStr)