import datetime
from peewee import *

DB = SqliteDatabase('tweet.db')

class BaseModel(Model):
    class Meta:
        database = DB

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    create_date = DateTimeField(default=datetime.datetime.now)

DB.create_tables([User, Tweet])

# #### Dasar Relasi Di Peewee

# data = (
#     ('Irine', ('Ini adalah twit Pertama', 'Ini manggung di Yogyakarta')),
#     ('Jenny', ('Ini adalah kursi', 'Ini manggung terus')),
#     ('Rose', ('Ini twit yang sangat bagus', 'Lagi dimana oy')),
#     ('Yeri', ('Pertama saya mau manggung', 'Bandung ajah lah'))
# )

# for username, tweets in data:
#     user = User.create(username = username)
#     for tweet in tweets:
#         Tweet.create(user=user, message=tweet)

