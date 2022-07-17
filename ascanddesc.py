from peewee import *
import random, datetime

db = SqliteDatabase('user.db')

class User(Model):
    username = CharField()
    point = IntegerField()
    join_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db 

db.connect()
db.create_tables([User], safe = True)

# #### Sorting Data ASC dan DESC

# untuk mensortir data dari kecil ke besar
# users = User.select().order_by(User.point)

# untuk mensortir data dari besar ke kecil
# users = User.select().order_by(User.point.desc())

# for user in users:
    # print(user.username + ' ' + str(user.point))

# def get_rand():
#     return random.randint(1, 30)

# data =  [
#     {'username' : 'Irine', 'point' : get_rand()},
#     {'username' : 'Joy', 'point' : get_rand()},
#     {'username' : 'Rose', 'point' : get_rand()},
#     {'username' : 'Jeny', 'point' : get_rand()}
# ]

# User.insert_many(data).execute()

# #### Update Data

# user = User.select().where(User.username == 'Rose').get()
# user.username = 'Rose Black Pink'
# user.save()

# User.update(point = 30).where(User.username == 'Jeny').execute()

# #### Menghapus Data

# user = User.get(User.id == 4)
# user.delete_instance()

# User.delete().where(User.point < 20).execute()