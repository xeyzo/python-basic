menus = ["chicken strip", "beef burger", "steakhouse", "mushroom swiss", "whopper"] # List A
price = [15,10,12,20,30] # List B

combine = dict(zip(menus, price))
asc = dict(sorted(combine.items(), key=lambda x: x[1]))    
print(asc)