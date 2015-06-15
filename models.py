__author__ = 'ed'
import datetime
from peewee import *
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash


DATABASE = SqliteDatabase('social.db')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    def get_posts(self):
        return Post.select().where(Post.user == self)

    def get_stream(self):
        return Post.select().where(
            (Post.user << self.following()) |
            (Post.user == self)
        )

    def following(self):
        """The users we are following"""
        return (
            User.select().join(
                Releationship, on=Releationship.to_user
            ).where(
                Releationship.from_user == self
            )
        )
    def followers(self):
        """get users following"""
        return (
            User.select().join(
                Releationship, on=Releationship.from_user
            ).where(
                Releationship.to_user == self
            )
        )

    def is_anonymous(self):
        return True


    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin
            )

        except IntegrityError:
            raise ValueError("user already exists")

class Post(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(
        rel_model=User,
        related_name='posts'

    )
    content = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)

class Releationship(Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    class Meta:
        database = DATABASE
        indexes = (
            (('from_user', 'to_user'), True)

        )





def initiliaze():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Releationship], safe=True)
    DATABASE.close()


