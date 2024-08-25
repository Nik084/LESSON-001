immutable_var = ['One', 'ty', 'treee'], 'text', 2.5, True, 101
print ('Immutable tuple:', immutable_var)
immutable_var [0][1] = immutable_var [0][1].replace('y', 'wo') # изменение содержимого списка, входящего в кортежь
immutable_var [0][1] = immutable_var [0][1].upper() # изменение регистра данных из списка, входящего в кортежь
print ('Immutable tuple:', immutable_var)
mutable_list = ['animal', 'street', 'tiger']
print ('Mutable list:', mutable_list)
mutable_list.remove('street')
mutable_list.append('leo')
print ('Mutable list:', mutable_list)
print (mutable_list [0].upper() + 'S:', str(mutable_list [1:3]))