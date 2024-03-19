'''
nested list
[2, [4, 6, [0]], [[[3]]], 10, [], [], 0]

flatten list
[2, 4, 6, 0, 3, 10, 0]
'''
nested_list = eval(input())
set =[]
for i in nested_list:
    set.append(i)
set = str(set)
flatten_string = set.replace(',', '').replace('[', '').replace(']', '')
flatten_list = list(map(int, flatten_string.split()))

print(flatten_list)