capitals = {'USA': 'Washington D.C.',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

'''
print(dir(capitals))
print(help(capitals))
print(capitals.get('USA'))

if capitals.get('Russia'):
    print('That capital exists')
else:
    print('That capital does not exist') 

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Detroit'})
capitals.pop('China')
capitals.popitem()
capitals.clear()
keys = capitals.keys()
values = capitals.values()
'''

items = capitals.items()
print(items)