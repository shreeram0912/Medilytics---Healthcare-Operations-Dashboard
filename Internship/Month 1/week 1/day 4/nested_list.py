nested_list = [[1,2],[3,4],[5,6], [7,8]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
    
print(flat_list)