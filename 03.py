text_1 = "Mammals"
text_2 = "Bruiser build"
frequencies = {} 
  
for char in text_1: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

print ("Per char frequency in '{}' is :\n {}".format(text_1, str(frequencies)))


for char in text_2: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

print ("Per char frequency in '{}' is :\n {}".format(text_2, str(frequencies)))
