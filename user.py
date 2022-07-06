from ast import For
from xml.sax.saxutils import prepare_input_source
from peewee import *

db = SqliteDatabase('user.db')

class User(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([User], safe = True) #untuk membuat table baru

# #### Insert Data

# insert satu data
# User.create(name = 'Irine', birthday = 'Inchon')

# insert banyak data
# data_resource = [
#     {'name' : 'Joy', 'birthday' : 'Soeul'},
#     {'name' : 'Mira', 'birthday' : 'Soeul'}
# ]

# print(User.insert_many(data_resource).execute())

# #### Memilih Data

# enaknya ini bisa di costume berdasarkan by id / name / birthday
# user = User.get(User.id == 6)
# print(user.name)

# kalau pake ini tidak bisa hanya bisa by id
# user = User.get_by_id(3)
# print(user)

# enaknya ini bisa di costume berdasarkan by id / name / birthday
# user = User[2]
# print(user.birthday)

# menampilkan semua data by id / name / birthday
# semuaData = User.select()
# for data in semuaData:
    #costume di sini
    # print(data.name)

# #### Filter Data Dengan Where

# users = User.select().where((User.name == 'Mira') | (User.name == 'Irine'))

# for user in users:
#     print(user.name)

# study kasus biasanya di gunakan ketika kita search data
# users = User.select().where(User.name.contains('Irine'))

# for user in users:
#     print(user.name)