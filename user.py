from peewee import *

db = SqliteDatabase('user.db')

class User(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([User], safe = True) #untuk membuat table baru

# insert satu data
# User.create(name = 'Irine', birthday = 'Inchon')

# insert banyak data
# data_resource = [
#     {'name' : 'Joy', 'birthday' : 'Soeul'},
#     {'name' : 'Mira', 'birthday' : 'Soeul'}
# ]

# print(User.insert_many(data_resource).execute())