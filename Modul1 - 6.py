my_dict = {'Anton': 1984, 'Boris': 1991, 'Pavel': 2001, 'Elena': 1989}
print ('Dictionary:', my_dict)
print ('Existing value:', my_dict['Pavel'])
print ('Not existing value (without error):', my_dict.get('Diana'))
my_dict.update({'Stepan': 1998, 'Alex': 1999})
print ('Deleted value:', my_dict.pop('Boris'))
print ('Modified dictionary:', my_dict)
my_set = {1, 3, 5, 7, 3, 5, 1, False, ('meat', 'meet')}
print ('Set:', my_set)
my_set.update({'dos', 3.11})
my_set.discard(('meat', 'meet'))
print ('Modified set:', my_set)