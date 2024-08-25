immutable_var = ['One', 'ty', 'treee'], 'text', 2.5, True, 101
print ('Immutable tuple:', immutable_var)
immutable_var [0][1] = immutable_var [0][1].replace('y', 'wo') # изменение содержимого списка, входящего в кортежь
immutable_var [0][1] = immutable_var [0][1].upper() # изменение регистра данных из списка, входящего в кортежь
print ('Immutable tuple:', immutable_var)
mutable_list = ['animal', 'street', 'tiger', 1988, 'snake']
print ('Mutable list:', mutable_list)
mutable_list[1] = 'leo'
mutable_list.append('panther')
mutable_list.remove(1988)
mutable_list.remove('snake')
mutable_list[0] = 'cats'
print ('Mutable list:', mutable_list)
# последняя строка вне задания. Сделана для повторения и закрепления пройденного.
print (mutable_list [0].upper() + ':', str(mutable_list [1]).title() + ',', str(mutable_list[2]).title() + ',', str(mutable_list[3]).title())