from tinydb import TinyDB, where
db = TinyDB('ab.json')
#db.insert({'int': 1, 'char': 'a'})
#db.insert({'int': 1, 'char': 'b'})
db.update({'char': 'c'}, where('int') == 1)
print (db.all())
