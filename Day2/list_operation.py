'''
today i'll learn list
'''

#creating a list

list_of_number = [1,2,3,4,5,6,7,8,9,10]
list_of_char = ['a','b','c','d','e','f','g','h']
list_of_mixed_type = [1,'a', [1,3,4,'a']]
list_empty = []

list_const = list('abcdefghi')

#list contructor 
print('Converting to a list object -> ',list_const)

#printing by index
print('printing by index -> ', list_of_mixed_type[2])

#printing by index on nested loop
print('printing by index on nested loop -> ', list_of_mixed_type[2][3])


#navigating by negative index
print('printing by negative index on nested loop -> ', list_of_number[-10])

#slicing a list 
print('Slicing a list -> ', list_of_char[1:3])

#adding or appending item on a list
# with or without mentioning the index, Append works with or without mentioning index
# if index is given then data will be inserted on specific index
list_of_char.append('j')
print('Appending item on a list -> ', list_of_char)
list_of_char.insert(0,'A')
print('Appending item on a list by index -> ', list_of_char)

#loop
for item in range(len(list_of_char)):
    print(item.index(list_of_char))